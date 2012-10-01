#coding:utf8
#Author:lvyaojia
#Date:2012.9.23

from options import parser
import logging
import requests
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse
from collections import deque
from urllib2 import quote

visitedHrefs = set()
unvisitedHrefs = deque()
logger = logging.getLogger()


def loggingConfig(logFile, logLevel):
    LEVELS={
        1:logging.CRITICAL,
        2:logging.ERROR,
        3:logging.WARNING,
        4:logging.INFO,
        5:logging.DEBUG,}
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    fileHandler = logging.FileHandler(logFile)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(LEVELS.get(logLevel))

def getHtml(url):
    '''
    根据url,获取html源代码
    '''
    #自定义header,防止被禁
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
            logger.info('Get links from : %s ' % url)
            print 'Get links from : %s ' % url
            try:
                return r.text
            except Exception,e:
                logger.error(e)
    return None

def getHrefs(url):
    '''
    解析html源码，获取其中的链接。 url参数用于处理相对链接。
    '''
    visitedHrefs.add(url)
    html = getHtml(url)
    if html == None or html == '' or url == None or url == '':
        return None
    soup = BeautifulSoup(html)
    results = soup.find_all('a',href=True)
    for a in results:
        #必须encode utf8 因为中文链接如 http://aa.com/文件.pdf 不会被url编码，从而导致encodeException
        href = a.get('href').encode('utf8')  
        #处理相对链接的问题
        if not href.startswith('http'):
            href = urljoin(url, href)
        #只获取http或https网页,去除如ftp://这样的链接
        if urlparse(href).scheme == 'http' or urlparse(href).scheme == 'https':
            if  href not in unvisitedHrefs and href not in visitedHrefs:
                unvisitedHrefs.append(href)


def getHrefsFromURL(url, depth):
    unvisitedHrefs.append(url)
    currentDepth = 1
    location = url
    flag = False

    #使用BFS算法， 用location标注每一层的最后一个链接。从而控制爬虫深度
    while currentDepth < depth+1:
        url = unvisitedHrefs.popleft()
        if location == url:
            flag = True
        
        getHrefs(url)

        if flag:
            flag = False
            logger.info('unvisitedHrefs: %d' % len(unvisitedHrefs))
            logger.info('visited: %d' % len(visitedHrefs))
            logger.info('====================Depth %d Finish ====================' % currentDepth)
            currentDepth += 1
            location = unvisitedHrefs[len(unvisitedHrefs)-1]

def main():
    #读取命令行参数
    args = parser.parse_args()
    url = args.url
    depth = args.depth
    logFile = args.logFile
    logLevel = args.logLevel

    loggingConfig(logFile, logLevel)

    if not url.startswith('http'):
        url = 'http://' + url
    getHrefsFromURL(url, depth)
    


if __name__ == '__main__':
    main()