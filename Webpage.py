#coding:utf8
#Authour:lvyaojia
#Date:2012.9.24



# def getHtml(url):
#         headers = {
#             'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
#             'Referer': url
#         }
#         req = urllib2.Request(
#             url = url,
#             headers = headers,
#         )
#         response = urllib2.urlopen(req)
#         html = response.read()
#         responseHeader = response.info().getheader('Content-Type')
#         response.close()
#         print responseHeader


class Webpage(object):

    _url = None
    _html = None
    _host = None
    _hrefs = None

    def __init__(self, url):
        self._url = url

    def initHtml(self):
        headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
            'Referer': self.url
        }
        req = urllib2.Request(
            url = self.url,
            headers = headers,
        )
        response = urllib2.urlopen(req)
        self._host = response.get_host()
        self._html = response.read()
        response.close()

    def initHrefs(self):
        if not self._html:
            pass
        else:
            soup = BeautifulSoup(self._html)
            results = soup.find_all('a',href=True)
            hrefs = []
            for a in results:
                href = a['href']
                #以#开头，页面内链接，不做处理
                if href.startswith('#'):
                    continue
                #处理以/开头的相对路径
                elif href.startswith('/'):
                    href = self._host + href
                #处理以.开头的相对路径
                elif href.startswith('.'):
                    href = url[0:url.rfind('/')+1] + href
                hrefs.append(href)
            self._hrefs = hrefs
        

    def getHtml(self):
        return self._html

    def getHrefs(self):
        return self._hrefs

