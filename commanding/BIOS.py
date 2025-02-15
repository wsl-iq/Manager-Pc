import time
import os
import sys

Running = "\033[94;1m" + '[Running]' + "\033[95;1m"

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

def BIOS_Loading():
    try:
        for i in range(1, 101):
            if i <= 25:
                color = G 
            elif i <= 50:
                color = B 
            elif i <= 75:
                color = Y 
            else:
                color = R
            
            print(f'{color}[{i}]% Loading Power off system and start open Bios')
            print(f'{Running} to exit press {R}[{Y}Ctrl {W}+ {Y}C{R}]{W}')
            time.sleep(0.09)
            os.system('cls' if os.name == 'nt' else 'clear')
    except KeyboardInterrupt:
        sys.exit()
if __name__ == '__main__':
    BIOS_Loading()

