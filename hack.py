from socket import *
import time

version = '1.0'

def ver():
  print("Hack version " +version)

def scan(target):
  t_IP = gethostbyname(target)
  startTime = time.time()
  print("Scanning " +t_IP)
    
  for i in range(50, 500):
    s = socket(AF_INET, SOCK_STREAM)
        
    conn = s.connect_ex((t_IP, i))
    if(conn == 0) :
      print ('Port %d: OPEN' % (i,))
      s.close()

  print('Time taken:', time.time() - startTime)

def connect():
  pass
