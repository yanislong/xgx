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
    url1 = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_wordseg"
    url2 = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_bcocr"
    url3 = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_bizlicenseocr"
    url4 = "https://api.ai.qq.com/fcgi-bin/ocr/ocr_idcardocr"
    data = {}
    data['app_id'] = "2109423791"
#    data['text'] = "腾讯人工智能".decode('utf-8').encode("GBK")
    data['time_stamp'] = int(time.mktime(time.localtime()))
    data['nonce_str'] = "247816734"
#    data['card_type'] = '0' #0,1
#    with open('./222.jpg','rb') as f:
#        base64_data = base64.b64encode(f.read())
    with open('./333.jpg','rb') as f:
        base64_data = base64.b64encode(f.read())
#    with open('./444.jpg','rb') as f:
#        base64_data = base64.b64encode(f.read())
    data['image'] = base64_data

    k = sorted(data)
    sk = map(lambda x:{x:data[x]},k)
#    data['sign'] = getReqSign(sk)
#    fanyin(data,url3)
