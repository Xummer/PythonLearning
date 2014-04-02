#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : multiprocess/multiPrint.py

import os
import threading
import multiprocessing

# worker
def worker(sign, lock):
	lock.acquire()
	print(sign, os.getpid())
	lock.release()

# Main
print ("main:", os.getpid())


# Multi-thread
record = []
lock = threading.Lock()
for i in range(5):
	thread = threading.Thread(target=worker, args=("thread", lock))
	thread.start()
	record.append(thread)

for thread in record:
	thread.join()


# Multi-process
record = []
lock = multiprocessing.Lock()
for i in range(5):
	process = multiprocessing.Process(target=worker, args=("process", lock))
	process.start()
	record.append(process)

for process in record:
	process.join()