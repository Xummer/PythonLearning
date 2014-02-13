#!/usr/bin/python
# Filename : if.py

number = 26
guess = int(raw_input('Enter an integer : '))

if guess == number:
  print 'Congratulations, you gessed it.'
  print '(but you do not win any prizes!)'
elif guess < number:
  print "No, it is a little higer than that"
else:
  print "No, it is a little lower than that"

print 'Done'
