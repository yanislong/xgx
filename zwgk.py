#!/usr/bin/env python

import re
import time
import sys

import bs4
import requests

import config

def getHtml(i=1):
    pageNum = i
    url = "http://zwgk.syx.gov.cn/pubjs/search.jsp?showsub=0&orderbysub=0&currpage=1" + str(i)
    header = {}
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    r = requests.get(url, headers=header)
    html = bs4.BeautifulSoup(r.content)
    return html

def getLink(i=1):
    html = getHtml(i)
    link = html.find_all(id="info")
    for i in link:
        reslink = i.a['href']
        getRes(reslink)

def getPageNum():
    global html
    pnum = html.find_all('table')
    for j in pnum[-2:-1]:
        p = j.tr.td.string
    l1 = re.compile(r'(\d+)')
    l2 = l1.findall(p)
    pageNum = int(l2[1])
#    print pageNum
    return pageNum

def getRes(url):
    header = {} 
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    r = requests.get(url, headers=header)
    html = bs4.BeautifulSoup(r.content)
    title = html.find_all('h2')
    body = html.find_all(class_="zwgk_lr")
#    print title[0].string
#    print body[0]
    con = str(body[0])
    conp = "<html><head><meta charset='utf-8'></head>" + con + "</html>"
    tt = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    name = title[0].string + tt
    with open('./document/' + name + '.html','w') as f:
        f.write(conp)

if __name__ == "__main__":
    html = getHtml()
    num = getPageNum()
    for i in (1,num):
        getLink(i)
