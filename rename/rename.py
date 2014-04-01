#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : rename.py

import os

# wrong
# from_name = "./\'test\'"
# to_name = "./\'test2\'"

from_name = "./test"
to_name = "./test2"

os.rename(from_name, to_name)
