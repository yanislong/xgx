#!/usr/bin/env python
#-*-coding=utf-8 -*-

import hashlib
import requests
import sys

def mm(v=None):
    vv = "123"#"20181015000219572" + str(v) + str("1435660288") + str("oRWgAl7wQTJ0AudWtblf")
    m = hashlib.md5()
    m.update(vv)
    print m.hexdigest()
    return m.hexdigest()


def fanyin(v):
    sign = mm(v)
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q=" + str(v) + "&from=en&to=zh&appid=20181015000219572&salt=1435660288&sign=" + str(sign)
    r = requests.get(url)
#    print r.content
    print "您输入的英文是: %s" %v
    print u"翻译结果为:\t" + r.json()['trans_result'][0]['dst']

#ss = sys.argv[1]
#fanyin(ss)
mm()
