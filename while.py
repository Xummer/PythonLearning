#!/usr/bin/python
# Filename : while.py

number = 26
running = True

while running:
  guess = int(raw_input('Enter an interger : '));
  
  if guess == number:
    print 'You get it'
    running = False
  elif guess < number:
    print 'NO, it is a little highjer than that'
  else:
    print 'NO, it is a little lower than that'
else:
  print 'The while loop is over.'

print 'Done'
