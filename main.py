#coding:utf8

import logging
import requests
import time
import re
import traceback
from datetime import datetime
from threading import Thread, Lock
from Queue import Queue,Empty
from options import parser
from database import Database
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque

#logger是全局的,线程安全
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
    try:
        fileHandler = logging.FileHandler(logFile)
    except IOError, e:
        return False
    else:
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(LEVELS.get(logLevel))
        return True

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
                func, args, kargs = self.threadPool.getTask(timeout=1)  #有可能Empty      
            except Empty:
                continue
            try:
                self.threadPool.increaseRunsNum() 
                result = func(*args, **kargs) #这里放容易阻塞线程的任务, 下载任务，文件IO
                self.threadPool.decreaseRunsNum()
                if result:
                    self.threadPool.putTaskResult(*result)
                self.threadPool.taskDone()
            except Exception, e:
                logger.critical(traceback.format_exc())

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

    def taskJoin(self, *args, **kargs):
        self.taskQueue.join()

    def taskDone(self, *args, **kargs):
        self.taskQueue.task_done()

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
        self.currentDepth = 1  #标注初始爬虫深度，从1开始
        self.keyword = args.keyword.decode('utf8') #指定关键词 #TODO,这里可能会出问题，因为win平台是gbk
        self.database =  Database(args.dbFile)#数据库
        self.threadPool = ThreadPool(args.threadNum)  #线程池,指定线程数
        self.visitedHrefs = set()    #已访问的链接
        self.unvisitedHrefs = deque()    #待访问的链接
        self.unvisitedHrefs.append(args.url) #添加首个待访问的链接

    def start(self):
        print '\nStart Crawling\n'
        if not self._isDatabaseAvaliable():
            print 'Error: Unable to open database file.'
        else:
            self.threadPool.startThreads() 
            self._startPrintProgress()   
            while self.currentDepth < self.depth+1:
                #分配任务,线程池并发下载当前深度的所有页面（该操作不阻塞）
                self._assignCurrentDepthTasks()
                #等待当前线程池完成所有任务
                #self.threadPool.taskJoin()可代替以下操作，可无法Ctrl-C Interupt
                while self.threadPool.getTaskLeft():
                    time.sleep(9)
                #当池内的所有任务完成时，即代表爬完了一个网页深度
                print 'Depth %d Finish. Totally visited %d links. \n' % (self.currentDepth, len(self.visitedHrefs))
                logger.info('-----Depth %d Finish. Total visited Links: %d-----\n' % (self.currentDepth, len(self.visitedHrefs)))
                #迈进下一个深度
                self.currentDepth += 1
            self.stop()

    def stop(self):
        print 'Stopping...\n'
        self.printProgress = False
        self.threadPool.stopThreads()
        self.database.close()

    def _assignCurrentDepthTasks(self):
        while self.unvisitedHrefs:
            url = self.unvisitedHrefs.popleft()
            self.threadPool.putTask(self._taskHandler, url)   #向任务队列分配任务
            self.visitedHrefs.add(url)  #标注该链接已被访问,或即将被访问,防止重复访问相同链接
 
    def _taskHandler(self, url):
        #先拿网页源码，再保存,两个都是高阻塞的操作，交给线程处理
        pageSource = self._getPageSource(url)
        if pageSource:
            self._saveTaskResults(url, pageSource)
            self._addUnvisitedHrefs(url, pageSource)

    def _getPageSource(self, url, retry=2):
        '''根据url,获取html源代码'''
        #自定义header,防止被禁,某些情况如豆瓣,还需制定cookies,否则被ban
        #设置了prefetch=False，当访问response.text 时才下载网页内容,避免下载非html文件
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
            'Referer': url,
        }
        try:
            response = requests.get(url, headers=headers, timeout=10, prefetch=False)
            if self._isResponseAvaliable(response, url):
                logger.debug('Get Page from : %s \n' % url)
                return response.text
            else:
                logger.warning('Page not avaliable. Status code:%d URL: %s \n' % (response.status_code, url) )
        except Exception,e:
            if retry>0: #超时重试
                return self._getPageSource(url, retry-1)
            else:
                logger.debug(str(e) + ' URL: %s \n' % (url))
                logger.debug(traceback.format_exc())
        return None

    def _isResponseAvaliable(self, response, url):
        #网页为200时再获取源码 (requests自动处理跳转)。只选取html页面。 
        if response.status_code == requests.codes.ok:
            if 'html' in response.headers['Content-Type']:
                return True
        return False

    def _saveTaskResults(self, url, pageSource):
        try:
            #使用正则的不区分大小写search比使用lower()后再查找要高效率
            if self.keyword:
                if re.search(self.keyword, pageSource, re.I):
                    self.database.saveData(url, pageSource, self.keyword) 
            else:
                self.database.saveData(url, pageSource)
        except Exception, e:
            logger.error(' URL: %s ' % url + traceback.format_exc())

    def _addUnvisitedHrefs(self, url, pageSource):
        '''添加未访问的链接。将有效的url放进UnvisitedHrefs列表'''
        #对链接进行过滤:1.只获取http或https网页;2.保证每个链接只访问一次
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
        return False

    def _isHrefRepeated(self, href):
        if href in self.visitedHrefs or href in self.unvisitedHrefs:
            return True
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

    def _isDatabaseAvaliable(self):
        if self.database.isConn():
            return True
        return False

    def selfTesting(self, args):
        url = 'http://www.baidu.com/'
        print '\nVisiting www.baidu.com'
        #测试网络,能否顺利获取百度源码
        pageSource = self._getPageSource(url)
        if pageSource == None:
            print 'Please check your network and make sure it\'s connected.\n'
        #测试日志保存
        elif not congifLogger(args.logFile, args.logLevel):
            print 'Permission denied: %s' % args.logFile
            print 'Please make sure you have the permission to save the log file!\n'
        #数据库测试
        elif not self._isDatabaseAvaliable():
            print 'Please make sure you have the permission to save data: %s\n' % args.dbFile
        else:
        #保存数据
            self._saveTaskResults(url, pageSource)
            print 'Create logfile and database Successfully.'
            print 'Already save Baidu.com, Please check the database record.'
            print 'Seems No Problem!\n'

def main():
    args = parser.parse_args()
    if not args.url.startswith('http'):
        args.url = 'http://' + args.url

    crawler = Crawler(args)

    if args.testSelf:
        crawler.selfTesting(args)
    elif not congifLogger(args.logFile, args.logLevel):
        print '\nPermission denied: %s' % args.logFile
        print 'Please make sure you have the permission to save the log file!\n'
    else:
        begin = datetime.now()
        crawler.start()
        end = datetime.now()
        print 'Begin:%s \n End:%s ' % (begin,end)
        print 'Spend time: %s '%(end-begin)

if __name__ == '__main__':
    main()