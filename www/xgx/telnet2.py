#!/usr/bin/env python
#-*-coding=utf-8 -*-

import urllib
import hashlib
import requests
import sys
import time
import random
import base64

def getReqSign(param,appkey="n1mbFkeW6EhRsaW9"):
    pp = ""
    for i in param:
        for i,k in i.items():
            if k != "":
                pp += str(i) + "=" + urllib.quote(str(k)).replace("/","%2F") + "&"
    sign = pp + "app_key=" + appkey
#    print sign
    m = hashlib.md5()
    m.update(sign)
#    print m.hexdigest().upper()
    return str(m.hexdigest().upper())

def fanyin(data,url):
    header = {}
    header['Content-Type'] = "application/x-www-form-urlencoded"
    r = requests.post(url, headers=header, data=data)
    print r.text

if __name__ == "__main__":
    url = "https://api.ai.qq.com/fcgi-bin/aai/aai_wxasrlong"
    data = {}
    data['app_id'] = "2109423791"
    data['time_stamp'] = int(time.mktime(time.localtime()))
    data['nonce_str'] = "247816734"
    data['format'] = 1 #[1,2,3,4]
    data['callback_url'] = '0'
    data['speech'] = '0'
    data['speech_url'] = '0'

    with open('./test.img','rb') as f:
        base64_data = base64.b64encode(f.read())
    data['speech'] = base64_data
    k = sorted(data)
    sk = map(lambda x:{x:data[x]},k)
    data['sign'] = getReqSign(sk)
    fanyin(data,url)
