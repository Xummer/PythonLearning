#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
import subprocess

def sha1File(filepath):
  sha = ["sha1sum", "openssl sha1"]
  for i in sha:
    cmd = "%s %s | egrep -o \"([A-Fa-z0-9]){40}\"" % (i, filepath)
    p = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p.wait()
    if p.returncode == 0:
      return p.stdout.readline()
      break

def main():
  if len(sys.argv) == 1:
    print "Please input 1 filepath at least"
  else:
    shasum = sha1File(sys.argv[1])
    print shasum

if __name__ == '__main__':
  main()
