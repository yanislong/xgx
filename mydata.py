#!/usr/bin/env python
#-*-coding=utf-8 -*-

import time
import pymysql

import config

def insertdb(**res):
    con = pymysql.connect(**config.mydb)
    cursor = con.cursor()
    ct = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    sql = "insert into zwgk(title, content, c_time) value(%s,%s,%s)"
    cursor.execute(sql,(res['title'],res['body'],ct))
    con.commit()
    cursor.close()
    con.close()

if __name__ == "__main__":
    r = {"title":"title","body":"content"}
    inertdb(**r)
