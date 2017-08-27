# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import re

def html_downloader():
    request = requests.Session()
    ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    headers = {'User-Agent' : ua,
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Connection': 'keep-alive'}
    request.headers = headers
    statue_code = 0
    url = raw_input('请输入需要采集数据的网页链接：')
    while statue_code == 0:
        try:
            response = request.get(url)
            if response.status_code == 200:
                print '网页链接正确'
                statue_code = 1
                return response.text, url
            else:
                url = raw_input('打开网页链接失败，请检查链接并重新输入：')
        except:
            url = raw_input('网页链接错误，请检查链接并重新输入：')

def html_parser(res, full_data, url):
    soup = BeautifulSoup(res, 'html.parser')
    if full_data == '1':
        try:
            img_content = soup.find('div', id="img-content")
            try:
                h2 = img_content.find('h2', class_="rich_media_title").text
                title = re.compile(u'\\r|\\n| ').sub('', h2)
            except:
                title = 'None'
            try:
                date = img_content.find('em', id="post-date", \
                    class_="rich_media_meta rich_media_meta_text").text
            except:
                date = 'None'
            try:
                author = img_content.find_all('em', \
                    class_="rich_media_meta rich_media_meta_text")[1].text
            except:
                author = 'None'
            try:
                post = img_content.find('a', id="post-user", class_=\
                "rich_media_meta rich_media_meta_link rich_media_meta_nickname").text
            except:
                post = 'None'
            for i in (title,date,author,post):
                print i 
        except:
            print '未找到目标数据，请手动打开网页检查。'
#         data = soup.text


if __name__ == '__main__':
    full_data = raw_input('是否全文下载?是请输入数字1，否请输入数字0：')
    res, url = html_downloader()
    html_parser(res, full_data, url)
    
    
    