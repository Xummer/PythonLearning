#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import subprocess

#print "%s" % platform.system()

def sha1File(filepath):
  sha = ["sh1sum", "openssl sha1"]
  for i in sha:
    cmd = "%s %s" % (i, filepath)
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p.wait()
    if p.returncode == 0:
      print "test ---"
      print p.stdout.readline()
      break

def main():
  if len(sys.argv) == 1:
    print "Please input 1 filepath at least"
  else:
    sha1File(sys.argv[1])

if __name__ == '__main__':
  main()
