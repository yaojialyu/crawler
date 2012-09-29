#coding:utf8
#Author:lvyaojia
#Date:2012.9.23

from options import parser
import logging
import requests
from bs4 import BeautifulSoup 
from urlparse import urljoin,urlparse



def getHtml(url):
    '''
    根据url,获取html源代码
    '''
    #给非http开头的url 加上http://
    if not url.startswith('http'):
        url = 'http://' + url
    #自定义header,防止被禁
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
        'Referer': url,
    }
    #doubancookies = dict(bid="sXP/lxGdf/o", ct="y", ll="118283", ck="38ij", __utma="30149280.775266482.1343046696.1348654603.1348664397.103", __utmb="30149280.4.10.1348664397", __utmc="30149280", __utmz="30149280.1348654603.102.21.utmcsr=s.weibo.com|utmccn=(referral)|utmcmd=referral|utmcct=/weibo/%25E8%25B1%2586%25E7%2593%25A3%2520%25E6%25A0%25A1%25E6%258B%259B&Refer=STopic_box", __utmv="30149280.153")
    try:
        #r = requests.get(url, headers=headers, timeout=10, prefetch=False,cookies=doubancookies)
        r = requests.get(url, headers=headers, timeout=10, prefetch=False,)
    except requests.exceptions.Timeout, e:
        print e
    except requests.exceptions.ConnectionError, e:
        print e
    else:
        #只抓取普通网页，避免访问图像或其它文件的链接。网页为200时再获取源代码 。设置了prefetch=False，当访问text 时才下载网页内容
        if r.headers['Content-Type'].find('html') != -1 and r.status_code == requests.codes.ok:
            return r.text
    return None

def getHrefs(html, url):
    '''
    解析html源码，获取其中的链接。 url参数用于处理相对链接。
    '''
    soup = BeautifulSoup(html)
    results = soup.find_all('a',href=True)
    #不放入重复的链接，选择set而非list
    hrefs = set()
    for a in results:
        href = a.get('href')
        #处理相对链接的问题
        if not href.startswith('http'):
            href = urljoin(url, href)
        #只获取http或https网页,去除如ftp://这样的链接
        if urlparse(href).scheme == 'http' or urlparse(href).scheme == 'https':
            hrefs.add(href)
    return hrefs


def main():
    #读取命令行参数
    args = parser.parse_args()
    url = args.url

    html = getHtml(url)
    #print html
    if html != None:
        hrefs = getHrefs(html, url)
        for h in hrefs:
            print h


if __name__ == '__main__':
    main()