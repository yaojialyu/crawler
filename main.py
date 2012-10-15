#coding:utf8

import logging
import requests
import time
from threading import Thread, Lock
from Queue import Queue
from options import parser
from database import Database
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque

def loggingConfig(logger, logFile, logLevel):
    '''配置logging的日志文件以及日志的记录等级'''
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
    def __init__(self, logger, args):
        self.depth = args.depth  #指定网页深度
        self.threadNum = args.threadNum #指定线程数
        self.keyword = args.keyword #指定关键词
        self.database = Database(args.dbFile) #数据库
        self.lock = Lock() #线程锁
        self.logger = logger #日志记录
        self.running = 0    #正在run的线程数
        self.currentDepth = 1  #标注初始爬虫深度，从1开始，非0开始
        self.visitedHrefs = set()    #已访问的链接
        self.unvisitedHrefs = deque()    #待访问的链接
        self.unvisitedHrefs.append(args.url) #添加首个待访问的链接
        self.taskQueue = Queue() #下载任务队列
        self.resultQueue = Queue() #下载任务结果队列
        self._initThreadPool()   #初始化线程池

    def start(self):
        print '\nStart Crawling\n'
        self._startPrintProgress()   #在Terminal定时打印信息

        while self.currentDepth < self.depth+1:
            #若没有需要访问的链接时break,防止网页没那么深，达不到depth要求时，造成阻塞
            if not self.unvisitedHrefs:
                break
            #将当前深度的所有链接都分配给任务队列
            self._assignUnvisitedHrefs()
            #从结果队列中获取当前深度的所有网页以及其包含的下个深度的链接
            self._handelTaskResults()
            #当以上两个任务完成时，即代表爬完了一个网页深度
            self.logger.info('-----Depth %d Finish. Total visited Links: %d-----' % (self.currentDepth, len(self.visitedHrefs)))
            print('Depth %d Finish. Totally visited %d Links\n' % (self.currentDepth, len(self.visitedHrefs)))
            #迈进下一个爬虫深度啦～～～
            self.currentDepth += 1
        self.stop()

    def _assignUnvisitedHrefs(self):
        while self.unvisitedHrefs:
            url = self.unvisitedHrefs.popleft()    
            self._assignTask(url)  #向任务队列分配下载任务
            self.visitedHrefs.add(url)  #标注该链接已被访问

    def _handelTaskResults(self):
        while self.getTaskLeft():
            #从结果队列获取并处理结果
            #若没有结果的话，会阻塞,直到线程下载完网页
            url, pageSource = self._getTaskResult() 
            #存放到数据库 这里没有使用多线程访问sqlite,因为不需要 
            if self.keyword:
                if pageSource.find(self.keyword) !=-1:
                    self.database.saveData(url, pageSource, self.keyword) 
            else:
                self.database.saveData(url, pageSource)
            #添加未访问的链接(先解析页面)
            self.addUnvisitedHrefs(url, pageSource) 

    def getTaskLeft(self):
        '''返回当前所有任务数'''
        return self.taskQueue.qsize()+self.resultQueue.qsize()+self.running

    def addUnvisitedHrefs(self, url, pageSource):
        '''过滤url,并将有效的url放进UnvisitedHrefs列表'''
        if pageSource != None and pageSource != '':
            hrefs = self._getAllHrefsFromPage(url, pageSource)
            #对链接进行过滤:1.只获取http或https网页;2.保证每个链接只访问一次
            for href in hrefs:
                if self._isHttpOrHttpsProtocol(href):
                    if not self._isHrefRepeated(href):
                        self.unvisitedHrefs.append(href)

    def _getAllHrefsFromPage(self, url, pageSource):
        '''解析html源码，获取页面所有链接。返回链接列表'''
        hrefs = []
        soup = BeautifulSoup(pageSource)
        #使用bs4查找页面内所有带链接的<a>标签
        results = soup.find_all('a',href=True)
        for a in results:
            #必须将链接encode为utf8, 因为中文文件链接如 http://aa.com/文件.pdf 在bs4中不会被自动url编码，从而导致encodeException
            href = a.get('href').encode('utf8')
            #处理相对链接的问题
            if not href.startswith('http'):
                href = urljoin(url, href)
            hrefs.append(href)
        return hrefs

    def _isHttpOrHttpsProtocol(self, href):
        protocal = urlparse(href).scheme
        if protocal == 'http' or protocal == 'https':
            return True
        else:
            return False

    def _isHrefRepeated(self, href):
        if href in self.unvisitedHrefs or href in self.visitedHrefs:
            return True
        else:
            return False

    def _startPrintProgress(self):
        '''创建线程,每隔10秒在屏幕上打印进度信息'''
        thread = Thread(target=self._printInfomation)
        thread.setDaemon(True)
        thread.start()

    def _printInfomation(self):
        while self.threadPool:  
            print '-------------------------------------------'
            print 'Crawling in depth %d' % self.currentDepth
            print 'Already visited %d Links' % (len(self.visitedHrefs)-self.getTaskLeft())
            print '%d tasks remaining in thread pool.' % self.getTaskLeft()
            print '-------------------------------------------\n'
            time.sleep(10)
                
    def _initThreadPool(self):
        self.threadPool = [] #线程池
        for i in range(self.threadNum):
            thread = Thread(target=self._doTasks)
            thread.setDaemon(True)
            self.threadPool.append(thread)
            thread.start()

    def stop(self):
        '''停止所有线程'''
        print 'Stop Crawling\n'
        for i in range(len(self.threadPool)):
            self._assignTask(None, 'stop')
        for thread in self.threadPool:
            thread.join()
        del self.threadPool[:]
        self.database.close()

    def _assignTask(self,url, command='start'):
        self.taskQueue.put((command, url))  #分配任务,command为start或stop

    def _getTask(self):
        return self.taskQueue.get()

    def _putTaskResult(self,taskResult):
        self.resultQueue.put(taskResult)

    def _getTaskResult(self):
        return self.resultQueue.get()

    def _doTasks(self):
        while 1:
            command, url = self._getTask()
            if command == 'stop':   #停止线程工作
                break
            try:
                if command == 'start':
                    self.lock.acquire() #保证操作的原子性，正在运行的线程数加1
                    self.running += 1 
                    self.lock.release()

                    pageSource = self._getPageSource(url)  #获取网页源码

                    self.lock.acquire() #下载任务完成，正在运行的线程数减1
                    self.running -= 1
                    self.lock.release()

                    self._putTaskResult((url, pageSource))  #将url与源码结果放入完成队列 
                else:
                    raise ValueError, 'Unknown command %r' % command
            except Exception,e:
                self.logger.critical(e)
            self.taskQueue.task_done()

    def _getPageSource(self, url):
        '''根据url,获取html源代码'''
        #自定义header,防止被禁,某些情况如豆瓣,还需制定cookies
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
            'Referer': url,
        }
        try:
            #发出请求。参数设置了prefetch=False，当访问response.text 时才下载网页内容,避免下载非html文件
            #TODO 超时没有重试,这里或许需要更改
            response = requests.get(url, headers=headers, timeout=10, prefetch=False)
        except Exception,e:
            #有可能网络连接出错，也有可能是网页无法访问(超时)
            self.logger.error(str(e) + ' URL: %s' % url)
        else:
            #只抓取普通网页，网页为200时再获取源代码 。        
            if response.headers['Content-Type'].find('html') != -1 and response.status_code == requests.codes.ok:
                self.logger.debug('Get Page from : %s ' % url)
                try:
                    return response.text
                except Exception,e:
                    self.logger.error(str(e) + ' URL: %s' % url)
            elif response.headers['Content-Type'].find('html') == -1:
                self.logger.debug('Not a normal Html page. URL: %s' % url)
            elif response.status_code != requests.codes.ok:
                self.logger.debug('Page cannot be visited successfully. Status Code:%d. URL:%s' % (response.status_code, url))
        return None

def main():
    args = parser.parse_args()
    if not args.url.startswith('http'):
        args.url = 'http://' + args.url

    logger = logging.getLogger()
    loggingConfig(logger, args.logFile, args.logLevel) 

    crawler = Crawler(logger, args)
    crawler.start()

if __name__ == '__main__':
    main()