import subprocess
import time
import os

G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[91;1m" + "ERROR" + "\033[93;1m" + " =>" + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"
other = "\033[95;1m" + "[" + "\033[93;1m" + "~" + "\033[95;1m" + "]" "\033[92;1m"
notice = Complete = "\033[94;1m" + "[" + "\033[92;1m" + "notice" + "\033[94;1m" + "]" + "\033[92;1m"

package = [
    "wmi",
    "psutil",
    "termcolor",
    "requests",
    "colorama",
    "prettytable",
    "rich",
    "rembg",
    "onnxruntime",
    "PyQt5",
    "Pillow",
    "numpy",
    "qrcode",
    "opencv-python",
    "decode",
    "pyzbar",
    "pygame",
    "speedtest-cli",
    "socks",
    "cfscrape",
    "httpx",
    "cloudscraper",
    "PySocks",
    "pyperclip",
    "win10toast",
    "tqdm",
    "instaloader",
    "keyboard"
]

os.system('cls' if os.name == 'nt' else 'clear')
for pip in package:
    subprocess.run(f'pip install {pip}', shell=True, check=True)

def slowprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
slowprint(f'{M}--------------- {Y}python upgrade {M}---------------{W}\n')
print(f'{INFO} {Y}=> {B}$ {G}python.exe -m pip install --upgrade pip{W}')
os.system('python.exe -m pip install --upgrade pip')
