'''
Created on Dec 1, 2015

@author: shenguanglin
'''
import NioThreadForTest
import redis
import time

threadDict = {}
#r = redis.Redis(host='192.168.1.139', port=6379, db=1,password="guyou@305A")
#r = redis.Redis(host='10.0.7.134', port=6379, db=1)
#url ="139.196.104.145"
url ="push.atlasyun.net"
index = 3
count = 15000
def start_nio():
    print("begin index:" + str(index*count) + ",to:" + str((index+1)*count))
    for i in range(index*count,(index+1)*count):
        niothread = NioThreadForTest.NioThread(i,"message simu", url, 18456)
        niothread.start()
        threadDict[i] = niothread
        time.sleep(0.01)
    pass
    print("thread create finished")
start_nio()
