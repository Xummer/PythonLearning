#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : multiprocess.py

from multiprocessing import Process, current_process

def test(inputpath, outputpath):
	p = current_process()
	print p.name, p.pid
	print inputpath, outputpath

def main():
	#test("X", "blabla")

	p = Process(target=test, args=("X", "output"), name ="test1")
	p.start()
	p.join()


if __name__ == '__main__':
	main()