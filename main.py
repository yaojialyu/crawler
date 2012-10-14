#coding:utf8

from threading import Thread, Lock
from Queue import Queue
from options import parser
import logging
import requests
import time
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque


def loggingConfig(logger, logFile, logLevel):
    '''
    配置logging的日志文件以及日志的记录等级
    '''
    LEVELS={
        1:logging.CRITICAL, 
        2:logging.ERROR,
        3:logging.WARNING,
        4:logging.INFO,
        5:logging.DEBUG,#数字最大记录最详细
        }

    formatter = logging.Formatter('%(asctime)s %(threadName)s %(levelname)s %(message)s')
    fileHandler = logging.FileHandler(logFile)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(LEVELS.get(logLevel))


class Crawler(object):
    def __init__(self, args, logger):
        self.depth = args.depth  #指定网页深度
        self.taskQueue = Queue() #下载任务队列
        self.resultQueue = Queue() #完成队列
        self.threadNum = args.threadNum #线程数
        self.threadPool = [] #线程池
        self.lock = Lock() #线程锁
        self.logger = logger #logging
        self.running = 0    #正在运行的线程数
        self.currentDepth = 1  #标注当前网页深度
        self.visitedHrefs = set()    #已访问的链接
        self.unvisitedHrefs = deque()    #待访问的链接
        self.unvisitedHrefs.append(args.url) #添加首个待访问的链接
        self.totalLinks = 0   #记录共访问了多少个页面
        self.__initThreadPool__()   #初始化线程池


    def start(self):
        print 'Start Crawling...'
        self.__startInformationTimer__()
        while self.currentDepth < self.depth+1:
            #若没有需要访问的链接时，则直接break,防止达不到depth要求时，进程阻塞
            if not self.unvisitedHrefs:
                break
            #将某个网页深度的所有链接都分配给任务队列
            while self.unvisitedHrefs:
                self.totalLinks += 1
                url = self.unvisitedHrefs.popleft()     #BFS算法
                self.__assignTask__(url)  #分配下载任务
                self.visitedHrefs.add(url)
            #获取某个深度的所有网页以及其包含的链接
            while self.taskleft():
                taskResult = self.__getTaskResult__()  #这里若没有结果的话，会阻塞
                self.addUnvisitedHrefsFromTaskResult(taskResult) 
            #当以上两个循环完成时，即代表爬完了一个网页深度
            logger.info('-----Depth %d Finish. Total visited Links: %d-----' % (self.currentDepth, self.totalLinks))
            print('-----Depth %d Finish. Total visited Links: %d-----' % (self.currentDepth, self.totalLinks))
            self.currentDepth += 1

        self.stop()

    def stop(self):
        print 'Stop Crawling...'
        for i in range(len(self.threadPool)):
            self.__assignTask__(None, 'stop')
        for thread in self.threadPool:
            thread.join()
        del self.threadPool[:]

    def taskleft(self):
        '''返回当前所有任务数'''
        count = self.taskQueue.qsize()+self.resultQueue.qsize()+self.running
        return count

    def getPageSource(self, url):
        '''根据url,获取html源代码'''
        #自定义header,防止被禁,某些情况如豆瓣,还需制定cookies
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
            'Referer': url,
        }
        try:
            #发出请求。参数设置了prefetch=False，当访问response.text 时才下载网页内容,避免下载非html文件
            response = requests.get(url, headers=headers, timeout=10, prefetch=False)
        except Exception,e:
            #有可能网络连接出错，也有可能是网页无法访问(超时)
            self.logger.error(str(e) + ' URL: %s' % url)
        else:
            #只抓取普通网页，网页为200时再获取源代码 。        
            if response.headers['Content-Type'].find('html') != -1 and response.status_code == requests.codes.ok:
                self.logger.debug('Get Page from : %s ' % url)
                #print 'Get Page from : %s ' % url
                try:
                    return response.text
                except Exception,e:
                    self.logger.error(str(e) + ' URL: %s' % url)
            elif response.headers['Content-Type'].find('html') == -1:
                self.logger.debug('Not a normal Html page for %s' % url)
            elif response.status_code != requests.codes.ok:
                self.logger.debug('Page cannot be visited successfully. Status Code:%d. URL:%s' % (response.status_code, url))
        return None

    def addUnvisitedHrefsFromTaskResult(self, taskResult):
        '''解析html源码，获取其中的链接。'''
        url, pageSource = taskResult
        if pageSource != None and pageSource != '':
            soup = BeautifulSoup(pageSource)
            #使用bs4查找页面内所有带链接的<a>标签
            results = soup.find_all('a',href=True)
            for a in results:
                #必须将链接encode为utf8, 因为中文文件链接如 http://aa.com/文件.pdf 在bs4中不会被自动url编码，从而导致encodeException
                href = a.get('href').encode('utf8')
                #处理相对链接的问题
                if not href.startswith('http'):
                    href = urljoin(url, href)
                #只获取http或https网页,去除如ftp://这样的链接
                if urlparse(href).scheme == 'http' or urlparse(href).scheme == 'https':
                    #保证每个链接只访问一次
                    if  href not in self.unvisitedHrefs and href not in self.visitedHrefs:
                        self.unvisitedHrefs.append(href)

    def __startInformationTimer__(self):
        '''创建新线程，每隔10秒在屏幕上打印进度信息'''
        thread = Thread(target=self.__showInfomation__)
        thread.setDaemon(True)
        thread.start()

    def __showInfomation__(self):
        while self.threadPool:  
            print 'Crawling in depth %d; Already visited %d Links; %d tasks remaining in thread pool.' \
            %(self.currentDepth, len(self.visitedHrefs)-self.taskleft(), self.taskleft())  
            time.sleep(10) 

    def __initThreadPool__(self):
        #初始化线程池
        for i in range(self.threadNum):
            thread = Thread(target=self.__doTasks__)
            thread.setDaemon(True)
            self.threadPool.append(thread)
            thread.start()

    def __assignTask__(self,url, command='start'):
        self.taskQueue.put((command, url))  #分配任务,command为start或stop

    def __getTaskResult__(self):
        return self.resultQueue.get()  #这里会Blocked,直到拿到网页源码为止

    def __doTasks__(self):
        while True:
            command, url = self.taskQueue.get() #这里也会Blocked
            if command == 'stop':
                break
            try:
                if command == 'start':
                    self.lock.acquire() #保证操作的原子性，正在运行的线程数+1
                    self.running += 1 
                    self.lock.release()

                    pageSource = self.getPageSource(url)  #获取网页源码

                    self.lock.acquire() #正在运行的线程数-1
                    self.running -= 1
                    self.lock.release()

                    self.resultQueue.put((url, pageSource))  #将源码结果放入完成队列
                    self.taskQueue.task_done()
                else:
                    raise ValueError, 'Unknown command %r' % command
            except Exception,e:
                self.logger.critical(e)


def main():
    args = parser.parse_args()
    if not args.url.startswith('http'):
        args.url = 'http://' + args.url

    logger = logging.getLogger()
    loggingConfig(logger, args.logFile, args.logLevel)  #初始化logging 模块

    crawler = Crawler(args, logger)
    crawler.start()

if __name__ == '__main__':
    main()