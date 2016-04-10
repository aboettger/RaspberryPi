#!/usr/bin/python
from Adafruit_CharLCD import Adafruit_CharLCD
import time , commands, re
lcd = Adafruit_CharLCD ()
lcd.begin (16,2)
while True:
  zeit = time. strftime("%y.%b %H:%M:%S")
  out = commands.getoutput("doveadm mailbox status all INBOX")
  m = re.search('.*unseen=(.+?) .*', out)
  print ("%s\nINBOX: %s" %(zeit , m.group(1)))
  # lcd.message ("%s\nINBOX: %s1f" %(zeit , temp [5:]))
  time.sleep (5)
  lcd.home ()
