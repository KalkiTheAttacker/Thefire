#!/usr/bin/python3

import socket 
import sys
import time 
import threading

usage = "python3 port.py TARGET START_PORT END_PORT"

print("-"*70)
print("A Simple Port Scanner By Karma")
print("-"*70)
if(len(sys.argv) != 4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name resolution error")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])
    
print("Scanning target", target)

def scan_port(port):
    print("Scanning port:", port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    conn = s.connect_ex((target, port))
    if not conn:
        print("port {} is OPEN".format(port))
    s.close()

for port in range(start_port, end_port+1):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
