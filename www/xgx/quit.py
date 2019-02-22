#!/usr/bin/python

import requests

def logout(ck):
    url = "http://zentao.hivescm.com:1080/zentao/user-logout.html"
    header = {}
    header['Cookie'] = ck
    r = requests.post(url, headers=header)
    print r.content


logout()


