#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : config/read_config.py

import ConfigParser

config = ConfigParser.ConfigParser()
with open("info", "rw") as cfgfile:
	config.readfp(cfgfile)

	name = config.get("info", "name")
	age = config.get("info", "age")
	txt = config.get("info", "text")

	print name, age, txt

