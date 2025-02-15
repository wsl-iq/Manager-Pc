import os
import sys
import shutil

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
ERROR = "\033[93;1m" + "×" + " " + "\033[91;1m" + "ERROR ⚠\n" + "\033[93;1m" + "╰─> " + "\033[93;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
Information = "\033[93;1m" + "[" + "\033[92;1m" + "Information" + "\033[93;1m" + "]" + "\033[94;1m"
Working = "\033[94;1m" + '[' + "\033[92;1m" + 'Working' + "\033[94;1m" + ']'
NotWorking = "\033[93;1m" + '[' + "\033[91;1m" + 'Not Working' + "\033[93;1m" + ']' + "\033[91;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
successfully = "\033[93;1m" + "[" + "\033[92;1m" + "successfully" + "\033[93;1m" + "]" + "\033[94;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"
other = "\033[95;1m" + "[" + "\033[93;1m" + "~" + "\033[95;1m" + "]" "\033[92;1m"
notice = "\033[94;1m" + "[" + "\033[92;1m" + "notice" + "\033[94;1m" + "]" + "\033[97;1m"
note = "\033[94;1m" + "[" + "\033[92;1m" + "note" + "\033[94;1m" + "]" + "\033[97;1m"
Running = "\033[94;1m" + '[Running]' + "\033[95;1m"
Ready = "\033[95;1m" + "[" + "\033[96;1m" + "Ready" + "\033[95;1m" + "]" + "\033[97;1m"
DONE = "\033[94;1m" + "[" + "\033[92;1m" + "DONE" + "\033[94;1m" + "]" + "\033[97;1m"
Loading = "\033[95;1m" + "[" + "\033[96;1m" + "Loading" + "\033[95;1m" + "]" + "\033[97;1m"
OK = "\033[92;1m" + "[" + "\033[94;1m" + "OK" + "\033[92;1m" + "]" + "\033[94;1m"
Okay = "\033[92;1m" + "[" + "\033[94;1m" + "Okay" + "\033[92;1m" + "]" + "\033[94;1m"
stop = "\033[91;1m" + '[' + "\033[93;1m" + 'stop' + "\033[91;1m" + ']' + "\033[95;1m"
Critical = "\033[95;1m" + "[" + "\033[96;1m" + "Critical" + "\033[95;1m" + "]" + "\033[97;1m"
paused = "\033[94;1m" + "[" + "\033[92;1m" + "paused" + "\033[94;1m" + "]" + "\033[92;1m"
Retrying = "\033[95;1m" + "[" + "\033[96;1m" + "Retrying" + "\033[95;1m" + "]" + "\033[97;1m"
Skip = "\033[95;1m" + "[" + "\033[96;1m" + "Skip" + "\033[95;1m" + "]" + "\033[97;1m"
SCAN = "\033[93;1m" + "[" + "\033[92;1m" + "SCAN" + "\033[93;1m" + "]" + "\033[94;1m"
Chacking = "\033[93;1m" + "[" + "\033[92;1m" + "Chacking" + "\033[93;1m" + "]" + "\033[94;1m"
Hacking = "\033[91;1m" + '[' + "\033[93;1m" + 'Hacking' + "\033[91;1m" + ']' + "\033[95;1m"
security = "\033[94;1m" + "[" + "\033[92;1m" + "security" + "\033[94;1m" + "]" + "\033[97;1m"
AI = "\033[95;1m" + "[" + "\033[96;1m" + "AI" + "\033[95;1m" + "]" + "\033[97;1m"

Black = "\033[40m"   # Black
Dark = "\033[40m"    # Dark
Red = "\033[41m"     # Red
Green = "\033[42m"   # Green
Yellow = "\033[43m"  # Yellow
Blue = "\033[44m"    # Blue
Magenta = "\033[45m" # Magenta
Cyan = "\033[46m"    # Cyan
White = "\033[47m"   # White
Reset = "\033[0m"    # Reset

def uninstall():
    try:
        while True:
            print(f' {G}[1] {B}Uninstall Manager PC{W}\n',f'{G}[2] {B}Exit{W}\n')
            
            uninstall_choice = input(f'{Enter} Enter your choice: {Y}')

            if uninstall_choice == '1':
                items_to_remove = [
                    'command',
                    'icon',
                    'PackageMicrosoft',
                    'server',
                    'html',
                    'About.txt',
                    'desktop.ini',
                    'setup.bat',
                    'run.exe'
                ]

                for item in items_to_remove:
                    if os.path.exists(item):
                        if os.path.isfile(item):
                            os.remove(item)
                            print(f'{INFO} File removed: {item}')
                        elif os.path.isdir(item):
                            shutil.rmtree(item)
                            print(f'{INFO} Folder removed: {item}')
                    else:
                        print(f'{please} Not found: {item}{W}')
                
                with open("cleanup.bat", "w") as batch_file:
                    batch_file.write(f"@echo off\n")
                    batch_file.write(f"timeout /t 2 >nul\n")
                    batch_file.write(f"del \"{__file__}\"\n")
                    batch_file.write(f"del cleanup.bat\n")
                
                print(f"{Running} Uninstallation complete Closing...{W}")
                
                os.system("start cleanup.bat")
                sys.exit()

            elif uninstall_choice == '2':
                print(f"{Running} Exiting...{W}")
                sys.exit()

            else:
                print(f"{ERROR} choice Please try again !{W}")
    except KeyboardInterrupt:
        print(f"\n{sign} Process interrupted by user.{W}")
        sys.exit()

if __name__ == '__main__':
    uninstall()
