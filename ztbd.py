#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
import json

import requests
import bs4

def getLink():
    url = "http://www.syx.gov.cn"
    url_home = url + "/page/item1666/index.html"
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    r = requests.get(url_home, headers=header)
    html = bs4.BeautifulSoup(r.content)
    hh = html.find_all(class_='tyym_left')
    zt = []
    for i in hh:
        for j in i.ul:
            try:
#                print j.a.string
#                print j.a['href']
                res = {"title": j.a.string,"link": url + j.a['href']}
                zt.append(res)
            except:
                break
#    print json.dumps(zt, ensure_ascii=False)
    return zt
    
def getRepon(**tl):
    print tl['title']
    url0 = "http://www.syx.gov.cn"
    url = "http://www.syx.gov.cn/addin/jslib/jquery/jpage/dataproxy.jsp?startrecord=0&endrecord=20&perpage=100"
    l1 = re.compile('\d{4}')
    l2 = l1.findall(tl['link'])
    header1 = {}
    header1['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    header = {}
    header['x-Requested-With'] = "XMLHTTPRequest"
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    data = {}
    data['appid'] = 1
    data['webid'] = 1
    data['path'] = "/"
    data['columnid'] = l2[0]
    data['sourceContentType'] = 1
    data['unitid'] = 12743
    data['webname'] = "邵阳县人民政府"
    data['permissiontype'] = 0
    r = requests.post(url, headers=header, data=data)
#    print r.content
    l1 = re.compile(r'<li><a(.*?)</a>')
    l2  = l1.findall(r.content)
    for i in l2:
        l1 = re.compile(r'">(.*?)$')
        l2 = l1.findall(i)
        l3 = re.compile(r'href="(.*?)"')
        l4 = l3.findall(i)
        url1 = url0 + l4[0]
        print "标题:\n" + l2[0]
        r1 = requests.get(url1, headers=header1)
        h = bs4.BeautifulSoup(r1.content)
        bb = h.find_all(style="text-align: left")
        try:
            print "内容:\n"  + str(bb[0])
        except IndexError:
            break

if __name__ == "__main__":
    for i in getLink():
        getRepon(**i)
        break
