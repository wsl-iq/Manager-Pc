import os
import sys
import requests
import time
from termcolor import colored

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
ERROR = "\033[93;1m" + "×" + " " + "\033[91;1m" + "ERROR\n" + "\033[93;1m" + "╰─> " + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"


def networking():
    def spin():
        delay = 0.25
        spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']
        for i in spinner:
            sys.stdout.write(f"\r{B}[*] Checking your internet connection... [{i}]{W}")
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\r\033[K")
        print(f"{G}[+] Your Internet connection has been verified.{W}")
        time.sleep(1)

    def check_internet_connection():
        try:
            response = requests.get('http://www.google.com', timeout=5)
            return True
        except requests.ConnectionError:
            return False

    while True:
        if check_internet_connection():
            spin()
            print(f"{sign} Internet connection is available. You can proceed with execution.{W}")
            time.sleep(0.25)
            os.system('control update')
            break

        else:
            print(f"{please} No internet connection!{W}")
            sys.exit()

if __name__ == '__main__':
    networking()