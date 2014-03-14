#!/usr/bin/python
# -*- coding: utf-8 -*
# Filename : mysql_connect.py

import MySQLdb

#SQL host

# 打开数据库连接
db = MySQLdb.connet("localhost","appadmin","admin","cptn");

# 使用cursor()获取操作游标
cursor = db.cursor();

# 使用execute 执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetchone()获取一条数据
data = cursor.fetchone()

print "Database version : %s " % data

#关闭数据库连接
db.close()
