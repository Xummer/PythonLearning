#!/usr/bin/env python
# -*- coding: utf-8 -*
# Filename : ffmpeg.py

import sys
import subprocess

defaultOutputPath = "."

# transcode video form |input.mp4| to |output.mpg|
def transcode(inputpath, outputpath = "./tmp.mpg"):
  cmd = '''
  ffmpeg -i \'%s\' -vcodec mpeg2video -b:v 5800k -qscale:v 2 -acodec libmp3lame -b:a 192k -f mpeg -vf scale=720:404,pad=720:576:0:86:black -aspect 4:3 -s 720x576 -r 25 -y \'%s\'
  ''' % (inputpath, outputpath)
  
  print cmd

  p = subprocess.Popen(
      cmd,
      shell=True,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)
  p.wait()

  if p.returncode == 0:
    print "transcode success"
    return 0
  else:
    print p.CalledProcessError()
    return 1

def main():
  sourcePath = "./movie.mp4"
  transcode(sourcePath)

if __name__ == '__main__':
  main()
