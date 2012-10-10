#coding:utf8
#Author:lvyaojia
#Date:2012.9.23

import threading, Queue, time, sys
from options import parser
import logging
import requests
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque
from urllib2 import quote

Lock = threading.Lock()
Jobs = Queue.Queue()
Pool = []
VisitedHrefs = set()
UnvisitedHrefs = deque()

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


def __getPageSource__(url):
    '''
    根据url,获取html源代码
    '''
    #自定义header,防止被禁,某些情况如豆瓣,还需制定cookies
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
        'Referer': url,
    }
    try:
        r = requests.get(url, headers=headers, timeout=10, prefetch=False,)
    except requests.exceptions.Timeout, e:
        logger.error(e)
    except requests.exceptions.ConnectionError, e:
        logger.error(e)
    else:
        #只抓取普通网页，避免访问图像或其它文件的链接。网页为200时再获取源代码 。设置了prefetch=False，当访问text 时才下载网页内容
        if r.headers['Content-Type'].find('html') != -1 and r.status_code == requests.codes.ok:
            logger.debug('Get links from : %s ' % url)
            try:
                return r.text
            except Exception,e:
                logger.error(e)
    return None

def getHrefs(url):
    '''
    解析html源码，获取其中的链接。 url参数用于处理相对链接。
    '''
    VisitedHrefs.add(url)
    html = __getPageSource__(url)
    if url == None or url == '':
        logger.warning('URL is illegal!!')
        return None
    elif html == None or html == '':
        logger.warning('Page may contain NOTHING, or it\'s not a normal Html page for %s' % url)
        return None
    else:
        soup = BeautifulSoup(html)
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
                if  href not in UnvisitedHrefs and href not in VisitedHrefs:
                    UnvisitedHrefs.append(href)


def doWorkFromJobs():
    while True:
        command, url = Jobs.get() 
        if command == 'stop':
            break
        try:
            if command == 'start':
                getHrefs(url)
            else:
                raise ValueError, 'Unknown command %r' % command
        except Exception,e:
            logger.critical(e)

def initThreadPool(threads, daemons=True):
    for i in range(threads):
         new_thread = threading.Thread(target=doWorkFromJobs)
         new_thread.setDaemon(daemons)
         Pool.append(new_thread)
         new_thread.start()

def requestWork(url, command='process'):
    Jobs.put((command, url))

def stopWorking():
    for i in range(len(Pool)):
        requestWork(None, 'stop')
    for thread in Pool:
        thread.join()
    del Pool[:]

#这里作为主线程
def getHrefsFromURL(url, depth):
    UnvisitedHrefs.append(url)
    currentDepth = 1
    location = url
    flag = False

    #使用BFS算法， 用location标注每一层的最后一个链接。从而控制爬虫深度
    while currentDepth < depth+1:
        url = UnvisitedHrefs.popleft()
        if location == url:
            flag = True
        
        #在这里可以分配任务给线程池
        requestWork(url)

        if flag:
            flag = False
            logger.info('Unvisited Links: %d' % len(UnvisitedHrefs))
            logger.info('Visited Links: %d' % len(VisitedHrefs))
            logger.info('**** Depth %d Finish ****' % currentDepth)
            currentDepth += 1
            location = UnvisitedHrefs[len(UnvisitedHrefs)-1]
    stopWorking()

def main():
    #读取命令行参数
    args = parser.parse_args()
    if not args.url.startswith('http'):
        args.url = 'http://' + args.url

    loggingConfig(args.logFile, args.logLevel)
    initThreadPool(args.threadNum, daemons=True)
    getHrefsFromURL(args.url, args.depth)
    


if __name__ == '__main__':
    main()