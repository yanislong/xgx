#!/usr/bin/env python
#-*-coding=utf-8 -*-

import requests
import bs4

def getRes(i=1):
    url = "http://www.syx.gov.cn/leadmail/front/findMail.do"
    header = {}
    header['x-Requested-With'] = "XMLHTTPRequest"
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    data = {}
    data['source'] = 1
    data['page'] = i
    data['rows'] = 10
    r = requests.post(url, headers=header, data=data)
    print r.content
    repon = r.json()["rows"]
    for i in repon:
        print i['mailtitle']
        print i['mailtext']
        print r"---------------分隔符------------------"

def getPageNum(i=1):
    url = "http://www.syx.gov.cn/leadmail/front/findMail.do"
    header = {}
    header['x-Requested-With'] = "XMLHTTPRequest"
    header['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
    data = {}
    data['source'] = 1
    data['page'] = i
    data['rows'] = 10
    r = requests.post(url, headers=header, data=data)
    pnum = r.json()['total']
    total = r.json()['records']
    return (pnum, total)

if __name__ == "__main__":
    pagenum = getPageNum()
    print "县长信箱总共有: %d 条数据，总共: %d 页" %(pagenum[1],pagenum[0])
    while True:
        num = int(raw_input("请输入查询到第多少页数据"))
        if num > 0 and num < pagenum[0]:
            break
    for i in (1,num):
        getRes(i)
