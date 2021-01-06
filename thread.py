#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:末夏
@file: thread.py
@time: 2021/01/06
"""
import threading
import os,time

balance=0
lock=threading.Lock()

def change(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_threading(n):
    for i in range(3000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


if __name__=="__main__":
    start_time=time.time()
    t1=threading.Thread(target=run_threading,args=(5,))
    t2=threading.Thread(target=run_threading,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time.time()
    print(balance,end_time-start_time)