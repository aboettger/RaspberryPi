import lcddriver
import time , commands, re

lcd = lcddriver.lcd()
lcd.lcd_clear()
while True:
  zeit = time.strftime("%a %d.%b %H:%M")
  out = commands.getoutput("su -c 'doveadm mailbox status all INBOX' aboettger")
  m = re.search('.*unseen=(.+?) .*', out)
  inbox = "{:<15}".format(m.group(1))
  lcd.lcd_display_string ("%s" %(zeit), 1)
  lcd.lcd_display_string ("%s %s" %("INBOX:", inbox), 2)
  time.sleep (10)
