#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : httplib_demo.py

import httplib, urllib

def httpGet():
	httpClient = None

	try:
		httpClient = httplib.HTTPConnection('www.baidu.com', timeout=30)
		httpClient.request('GET', '/')

		response = httpClient.getresponse()
		print response.status
		print response.reason
		print response.read()

	except Exception, e:
		print e
	finally:
		if httpClient:
			httpClient.close()

def httpPost():
	httpClient = None

	try:
		params = urllib.urlencode({'name': 'xummer', 'age': 24})
		headers = {"Content-type": "application/x-www-form-urlencoded", 
					"Accept": "text/html"}

		httpClient = httplib.HTTPConnection('localhost', 8888, timeout=30)
		httpClient.request('POST', '/test/index.php', params, headers)

		response = httpClient.getresponse()
		print response.status
		print response.reason
		print response.read()
		print response.getheaders() #获取头信息

	except Exception, e:
		print e
	finally:
		if httpClient:
			httpClient.close()

def main():
	httpPost()

if __name__ == '__main__':
	main()