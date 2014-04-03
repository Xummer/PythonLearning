#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : kill_process_from_thread.py

import os,signal
import threading
import time

def heatbeat(start_time):
	timeout_duration = 20
	while True:
		current_time = time.time()

		if (current_time-start_time) > timeout_duration:
			# timeout kill current process
			pid = os.getpid()
			print "kill <pid %d>" % pid

			try:
				# run |kill -l| in terminal to get all signal
				os.kill(pid, signal.SIGKILL) 
			except Exception, e:
				print e
				#raise e
			finally:
				break
			

		else:
			print "---> %d" % current_time

		time.sleep(1)

def main():
	print "- start -"

	# do something

	heartbeat_thread = threading.Thread(target=heatbeat, args=(time.time(),))
	heartbeat_thread.start()

	time.sleep(100)

main()
	
