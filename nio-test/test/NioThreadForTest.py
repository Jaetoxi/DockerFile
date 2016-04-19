'''
Created on Sep 3, 2015

@author: shenguanglin
'''
from socket import *
import time
import threading
import json

class NioThread(threading.Thread):
    def __init__(self, uid, message, host, port):
        threading.Thread.__init__(self)
        self._uid = uid
        self._message = message
        self._host = host
        self._port = port

    def stop(self):
        self._stop.set()
        self.is_running = False

    def onlyCharNum(self, s,oth=''):
        s = s.lower();
        fomart = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz013456789:{},-_//"'
        for c in s:
            if not c in fomart:
                s = s.replace(c,'');
        return s;
    def stopped(self):
        return self._stop.isSet()

    def close(self):
        self.tcpCliSock.close()
        self.shutdown(socket.SHUT_RD)

    def run(self):
        self.tcpCliSock = socket(AF_INET, SOCK_STREAM)
        self.tcpCliSock.connect((self._host, self._port))
        #self.tcpCliSock.settimeout(5)
        data = ('%s{"uid":%d,"type": 257,"rid": 1,"msg":"%s","data":{"token":"%s"}}%s')%('\r\n\r\n0001',int(self._uid), self._message, self._uid,'\r\n')
        self.tcpCliSock.send(data.encode())

        try :
            self.is_running = True
            self.cur_ts =time.time()
            while self.is_running:
                try:
                    if self.is_running:
                        recv_data=self.tcpCliSock.recv(1024)
                        if len(recv_data) > 0:
                            #print(self._uid, "Receive Data,len[ " + str(len(recv_data)) + "]," + self.onlyCharNum(str(recv_data[8:-2])))
                            package = recv_data[8:-1]
                            i = 0
                            for c in package:
                                i = i + 1
                                if c == '\r':
                                    package = package[0:i]
                                    try:
                                        data_string = json.loads(str(package))
                                        if data_string['type'] < 256:
                                            print str(package)
                                    except:
                                        print(self._uid, "Receive Data:[" + str(package) + "]")
                    else:
                        data = ('%s{"uid":%d,"type": 258,"rid": 1,"msg":"%s"}%s')%('\r\n\r\n0001',int(self._uid), self._message,'\r\n')
                        self.tcpCliSock.send(data.encode())
                        self.cur_ts =time.time()
                        #print("send heatbeat package")
                except timeout:
                    continue


            self.tcpCliSock.close()
        except Exception as ex:
            print ("{" + "error:[" + str(self._uid)+ "]" + str(ex) + "}")
  
