#coding:utf8
#Author:lvyaojia
#Date:2012.9.23

from threading import Thread, Lock
from Queue import Queue
from options import parser
import logging
import requests
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque
from urllib2 import quote


#logger 为全局变量——线程安全
#The logging module is intended to be thread-safe without any special work 
#needing to be done by its clients. It achieves this though using threading 
#locks; there is one lock to serialize access to the module’s shared data, and 
#each handler also creates a lock to serialize access to its underlying I/O.
logger = logging.getLogger()


def loggingConfig(logFile, logLevel):
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

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    fileHandler = logging.FileHandler(logFile)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(LEVELS.get(logLevel))


class Downloader(object):
    def __init__(self, args, logger):
        self.taskQueue = Queue() #下载任务队列
        self.resultQueue = Queue() #完成队列
        self.threadNum = args.threadNum #线程数
        self.threadPool = [] #线程池
        self.lock = Lock() #线程锁
        self.logger = logger #logging
        self.running = 0    #正在运行的线程数
        self.__initThreadPool__()   #初始化线程池

    def getCurrentTaskCount(self):
        return self.taskQueue.qsize()+self.resultQueue.qsize()+self.running

    def assignTask(self,url, command='start'):
        self.taskQueue.put((command, url))

    def getTaskResult(self):
        return self.resultQueue.get()  #这里或者会Blocked掉,因此主线程就不会一直跑

    def stopWorking(self):
        for i in range(len(self.threadPool)):
            self.assignTask(None, 'stop')
        for thread in self.threadPool:
            thread.join()
        del self.threadPool[:]

    def __initThreadPool__(self):
        for i in range(self.threadNum):
             thread = Thread(target=self.__doTasks__)
             thread.setDaemon(True)
             self.threadPool.append(thread)
             thread.start()
             #self.logger.debug('start thread: %s' % i) #thread 有自己的名称

    def __doTasks__(self):
        while True:
            command, url = self.taskQueue.get() #这里也会Blocked
            if command == 'stop':
                break
            with self.lock: #保证操作的原子性，正在运行的线程数+1
                self.running += 1 
            try:
                if command == 'start':
                    pageSource = self.__getPageSource__(url)
                    self.resultQueue.put((url, pageSource))
                else:
                    raise ValueError, 'Unknown command %r' % command
            except Exception,e:
                self.logger.critical(e)
            with self.lock: #保证操作的原子性，正在运行的线程数-1
                self.running -= 1 
            self.taskQueue.task_done()

    def __getPageSource__(self, url):
        '''
        根据url,获取html源代码
        '''
        #自定义header,防止被禁,某些情况如豆瓣,还需制定cookies
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
            'Referer': url,
        }
        try:
            response = requests.get(url, headers=headers, timeout=10, prefetch=False)
        except Exception,e:
            self.logger.error(e + '\nURL: %s' % url)
        else:
            #只抓取普通网页，避免访问图像或其它文件的链接。网页为200时再获取源代码 。设置了prefetch=False，当访问text 时才下载网页内容
            if response.headers['Content-Type'].find('html') != -1 and response.status_code == requests.codes.ok:
                self.logger.debug('Get Page from : %s ' % url)
                print 'Get Page from : %s ' % url
                try:
                    return response.text
                except Exception,e:
                    self.logger.error(e)
        return None


def getHrefs(taskResult):
    '''
    解析html源码，获取其中的链接。 url参数用于处理相对链接。
    '''
    url, pageSource = taskResult
    if pageSource == None or pageSource == '':
        logger.warning('Page may contain NOTHING, or it\'s not a normal Html page for %s' % url)
        return None
    else:
        soup = BeautifulSoup(pageSource)
        #使用bs4查找页面内所有带链接的<a>标签
        results = soup.find_all('a',href=True)
        for a in results:
            #必须将链接encode为utf8, 因为中文文件链接如 http://aa.com/文件.pdf 不会被自动url编码，从而导致encodeException
            href = a.get('href').encode('utf8')
            #处理相对链接的问题
            if not href.startswith('http'):
                href = urljoin(url, href)
            #只获取http或https网页,去除如ftp://这样的链接
            if urlparse(href).scheme == 'http' or urlparse(href).scheme == 'https':
                if  href not in unvisitedHrefs and href not in visitedHrefs:
                    unvisitedHrefs.append(href)
    

visitedHrefs = set()    #已访问的链接
unvisitedHrefs = deque()    #待访问的链接

#主线程
def main():
    #读取命令行参数
    args = parser.parse_args()
    if not args.url.startswith('http'):
        args.url = 'http://' + args.url
    #配置logging
    loggingConfig(args.logFile, args.logLevel)

    currentDepth = 1    #标注当前深度
    location = args.url #每个深度的最后一个链接,这里代表第一层的最后一个链接（只有一个根链接）
    flag = False

    downloader = Downloader(args, logger)
    unvisitedHrefs.append(args.url) 

    #使用BFS算法， 用location标注每一层的最后一个链接。从而控制爬虫深度
    while currentDepth < args.depth+1:
        url = unvisitedHrefs.popleft()
        if location == url:
            flag = True
        
        #在这里可以分配任务给线程池
        downloader.assignTask(url)
        getHrefs(downloader.getTaskResult())

        if flag:
            flag = False
            logger.info('Unvisited Links: %d' % len(unvisitedHrefs))
            logger.info('Visited Links: %d' % len(visitedHrefs))
            logger.info('**** Depth %d Finish ****' % currentDepth)
            currentDepth += 1
            location = unvisitedHrefs[len(unvisitedHrefs)-1]
    downloader.stopWorking()
    


if __name__ == '__main__':
    main()