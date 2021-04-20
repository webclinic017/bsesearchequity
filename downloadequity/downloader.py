#!/usr/bin/env python3


import redis
import os
import csv
redis_host = "localhost"
redis_port = 6379
redis_password = ""
import glob
from datetime import date


def downloaddata():
    today = str(date.today())
    listdate=(today.split("-"))

    filename=listdate[2]+listdate[1]+listdate[0][2:]
    os.system("wget https://www.bseindia.com/download/BhavCopy/Equity/EQ"+filename+"_CSV.ZIP")

    os.system("unzip -o *ZIP")


def readcsvandwritetoredis():
    import glob
    r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    myhashmap = {}
    for each in glob.glob("*CSV"):
        fd=open(each,"rt")
        data=csv.reader(fd)

        for row in data:

           localhashmap={}
           localhashmap["open"]=row[4]
           localhashmap["high"]=row[5]
           localhashmap["low"] = row[6]
           localhashmap["close"] = row[7]
           localhashmap["code"] = row[0]

           r.hmset(str(row[1]),localhashmap)

        print("now read data from redis")
        fd=open(each,"rt")
        data=csv.reader(fd)

        for row in data:


           output=r.hmget(str(row[1]),"open","high","low","close","code")
           print("myoutput",output)











if __name__ == '__main__':
    downloaddata()
    readcsvandwritetoredis()

