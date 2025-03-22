import os
import subprocess
from datetime import datetime

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
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "×" + " " + "\033[91;1m" + "ERROR\n" + "\033[93;1m" + "╰─> " + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
Working = "\033[94;1m" + '"\033[96;1m"' + 'Working' + "\033[94;1m" + ']'
NotWorking = "\033[93;1m" + '[' + "\033[91;1m" + 'Not Working' + "\033[93;1m" + ']' + "\033[91;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"
other = "\033[95;1m" + "[" + "\033[93;1m" + "~" + "\033[95;1m" + "]" "\033[92;1m"
notice = Complete = "\033[94;1m" + "[" + "\033[92;1m" + "notice" + "\033[94;1m" + "]" + "\033[92;1m"
Running = "\033[94;1m" + '[Running]' + "\033[95;1m"

def DateTime():
    try:
        times = datetime.now()
        formatted_time = times.strftime("%I:%M %p")
        formatted_day = times.strftime("%A")
        date_day = (
            "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" +
            "\033[97;1m" + "(" + "\033[93;1m" + formatted_day +
            "\033[95;1m" + f" {times:%B %d %Y}" +
            "\033[97;1m" + ")" + "\033[94;1m" + "[" +
            "\033[92;1m" + "Time" + "\033[94;1m" + "]" +
            "\033[93;1m" + "[" + "\033[91;1m" + formatted_time +
            "\033[93;1m" + "]" + "\033[97;1m"
        )
        print(date_day)
    except Exception as e:
        print(ERROR(str(e)))

def list_outdated_apps():
    try:
        print("\033[97;1m")
        result = subprocess.run(["winget", "upgrade"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(ERROR(str(e)))

def update_outdated_apps():
    try:
        print("\033[97;1m")
        result = subprocess.run(["winget", "upgrade", "--all"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(ERROR(str(e)))

def winget():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            DateTime()
            print(f"{G}[1] {B}List outdated apps{W}")
            print(f"{G}[2] {B}Update outdated apps{W}")
            print(f"{G}[3] {B}Update all apps{W}")
            choice = input(f"{Enter} Enter choice for your options:{Y} ")
    
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[97;1m")
                DateTime()
                list_outdated_apps()
                break

            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[97;1m")
                update_outdated_apps()
                break

            elif choice == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\033[97;1m")
                DateTime()
                update_outdated_apps()
                break

            else:
                print(f"{please} Error choice please Try again!{W}")
                continue

    except Exception as e:
        print(ERROR(str(e)))

if __name__ == "__main__":
    winget()