#coding:utf8
#Author:lvyaojia
#Date:2012.9.23

from options import parser
import requests
from bs4 import BeautifulSoup 


def getHtml(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
        'Referer': url
    }
    try:
        r = requests.get(url, headers=headers, timeout=10, prefetch=False)
    except requests.exceptions.Timeout, e:
        print e
    except requests.exceptions.ConnectionError, e:
        print e
    else:
        #只抓取普通网页，避免访问图像或其它文件的链接, 设置了prefetch=False，当访问text 时才下载网页内容
        if r.headers['Content-Type'].find('html') != -1 and r.status_code == requests.codes.ok:
            return r.text
    return None

def getHrefs(html):
    pass


def main():
    #读取命令行参数
    args = parser.parse_args(['-u', 'http://baidu.com', '-d', '2'])
    html = getHtml(args.url)
    print html


    
    


if __name__ == '__main__':
    main()