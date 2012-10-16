#coding:utf8

import logging
import requests
import time
from threading import Thread, Lock
from Queue import Queue,Empty
from options import parser
from database import Database
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque

class Worker(Thread):
    def __init__(self, threadPool):
        Thread.__init__(self)
        self.threadPool = threadPool
        self.daemon = True
        self.state = None
        self.start()

    def stop(self):
        self.state = 'STOP'

    def run(self):
        while 1:
            if self.state == 'STOP':
                break
            try:
                func, args, kargs = self.threadPool.getTask(timeout=1)
            except Empty:
                continue
            try:
                self.threadPool.increaseRunsNum()  
                result = func(*args, **kargs) #这里放容易阻塞线程的任务，在这下载web
                self.threadPool.decreaseRunsNum()
                self.threadPool.putTaskResult(*result)
            except Exception, e: 
                logger.error(str(e))

class ThreadPool(object):
    def __init__(self, threadNum):
        self.pool = [] #线程池
        self.threadNum = threadNum  #线程数
        self.lock = Lock() #线程锁
        self.running = 0    #正在run的线程数
        self.taskQueue = Queue() #任务队列
        self.resultQueue = Queue() #结果队列
    
    def startThreads(self):
        for i in range(self.threadNum): 
            self.pool.append(Worker(self))
    
    def stopThreads(self):
        for thread in self.pool:
            thread.stop()
            thread.join()
        del self.pool[:]
    
    def putTask(self, func, *args, **kargs):
        self.taskQueue.put((func, args, kargs))

    def getTask(self, *args, **kargs):
        return self.taskQueue.get(*args, **kargs)

    def putTaskResult(self, *args):
        self.resultQueue.put(args)

    def getTaskResult(self, *args, **kargs):
        return self.resultQueue.get(*args, **kargs)

    def increaseRunsNum(self):
        self.lock.acquire() #锁住该变量,保证操作的原子性
        self.running += 1 #正在运行的线程数加1
        self.lock.release()

    def decreaseRunsNum(self):
        self.lock.acquire() 
        self.running -= 1 
        self.lock.release()

    def getTaskLeft(self):
        #线程池的所有任务包括：taskQueue中未被下载的任务, resultQueue中完成了但是还没被取出的任务, 正在运行的任务（running）
        #因此任务总数为三者之和
        return self.taskQueue.qsize()+self.resultQueue.qsize()+self.running

class Crawler(object):
    def __init__(self, args):
        self.depth = args.depth  #指定网页深度
        self.keyword = args.keyword.decode('utf8') #指定关键词 #TODO,这里可能会出问题，因为win平台是gbk
        self.database = Database(args.dbFile) #数据库
        self.threadPool = ThreadPool(args.threadNum)  #线程池,指定线程数
        self.currentDepth = 1  #标注初始爬虫深度，从1开始
        self.visitedHrefs = set()    #已访问的链接
        self.unvisitedHrefs = deque()    #待访问的链接
        self.unvisitedHrefs.append(args.url) #添加首个待访问的链接

    def start(self):
        print '\nStart Crawling\n'
        self.threadPool.startThreads() #启动线程池
        self._startPrintProgress()   #在Terminal定时打印信息
        while self.currentDepth < self.depth+1:
            #没有需要访问的链接时就停下
            if not self.unvisitedHrefs:
                break
            #分配任务,并发下载当前深度的所有页面
            self._assignCurrentDepthTasks()
            #处理当前深度的所有页面
            self._handelCurrentDepthTaskResults()
            #当以上两个任务完成时，即代表爬完了一个网页深度
            logger.info('-----Depth %d Finish. Total visited Links: %d-----' % (self.currentDepth, len(self.visitedHrefs)))
            print('Depth %d Finish. Totally visited %d Links\n' % (self.currentDepth, len(self.visitedHrefs)))
            #迈进下一个深度
            self.currentDepth += 1
        self.stop()

    def stop(self):
        self.printProgress = False
        self.threadPool.stopThreads()
        self.database.close()
        print 'Finish! Stop Crawling.\n'

    def _assignCurrentDepthTasks(self):
        while self.unvisitedHrefs:
            url = self.unvisitedHrefs.popleft()
            self.threadPool.putTask(self._getPageSource, url)   #向任务队列分配下载任务
            self.visitedHrefs.add(url)  #标注该链接已被访问

    def _handelCurrentDepthTaskResults(self):
        '''从结果队列获取并处理结果（保存网页，抽取网页上有效的链接）'''
        #只要线程池还有任务，就继续处理
        while self.threadPool.getTaskLeft():
            #一旦有线程下载完，就立刻拿出结果来处理
            url, pageSource = self.threadPool.getTaskResult()
            if pageSource: 
                if self.keyword:
                    if pageSource.find(self.keyword) !=-1:
                        self.database.saveData(url, pageSource, self.keyword) 
                else:
                    self.database.saveData(url, pageSource)
                #添加未访问的链接
                self._addUnvisitedHrefs(url, pageSource) 

    def _addUnvisitedHrefs(self, url, pageSource):
        '''过滤url,并将有效的url放进UnvisitedHrefs列表'''
        #对链接进行过滤:1.只获取http或https网页;2.保证每个链接只访问一次
        if pageSource != None and pageSource != '':
            hrefs = self._getAllHrefsFromPage(url, pageSource)
            for href in hrefs:
                if self._isHttpOrHttpsProtocol(href):
                    if not self._isHrefRepeated(href):
                        self.unvisitedHrefs.append(href)

    def _getAllHrefsFromPage(self, url, pageSource):
        '''解析html源码，获取页面所有链接。返回链接列表'''
        hrefs = []
        soup = BeautifulSoup(pageSource)
        results = soup.find_all('a',href=True)
        for a in results:
            #必须将链接encode为utf8, 因为中文文件链接如 http://aa.com/文件.pdf 
            #在bs4中不会被自动url编码，从而导致encodeException
            href = a.get('href').encode('utf8')
            if not href.startswith('http'):
                href = urljoin(url, href)#处理相对链接的问题
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
        self.printProgress = True
        thread = Thread(target=self._printInfomation)
        thread.setDaemon(True)
        thread.start()

    def _printInfomation(self):
        while self.printProgress:  
            print '-------------------------------------------'
            print 'Crawling in depth %d' % self.currentDepth
            print 'Already visited %d Links' % (len(self.visitedHrefs)-self.threadPool.getTaskLeft())
            print '%d tasks remaining in thread pool.' % self.threadPool.getTaskLeft()
            print '-------------------------------------------\n'
            time.sleep(10)

    def _getPageSource(self, url):
        '''根据url,获取html源代码'''
        #自定义header,防止被禁,某些情况如豆瓣,还需制定cookies,否则被ban
        #设置了prefetch=False，当访问response.text 时才下载网页内容,避免下载非html文件
        #只抓取普通网页，网页为200时再获取源代码 。
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
            'Referer': url,
        }
        try:
            #TODO 超时没有重试,这里或许需要更改.超时重试3次
            response = requests.get(url, headers=headers, timeout=15, prefetch=False)
        except Exception,e:
            logger.error(str(e) + ' URL: %s' % url)
        else:  
            if response.headers['Content-Type'].find('html') != -1 and response.status_code == requests.codes.ok:
                logger.debug('Get Page from : %s ' % url)
                try:
                    return url, response.text
                except Exception,e:
                    logger.error(str(e) + ' URL: %s' % url)
            elif response.headers['Content-Type'].find('html') == -1:
                logger.debug('Not a normal Html page. URL: %s' % url)
            elif response.status_code != requests.codes.ok:
                logger.debug('Page cannot be visited successfully. Status Code:%d. URL:%s' % (response.status_code, url))
        return url,None

logger = logging.getLogger()

def congifLogger(logFile, logLevel):
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

def main():
    args = parser.parse_args()
    if not args.url.startswith('http'):
        args.url = 'http://' + args.url
    congifLogger(args.logFile, args.logLevel)
    crawler = Crawler(args)
    crawler.start()

if __name__ == '__main__':
    main()