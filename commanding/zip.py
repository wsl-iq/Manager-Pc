import os
import time
import sys
import zipfile
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
        print(str(e))

def Back_Menu():
    try:
        while True:
            Back = input(f'{Question} Do You Go To Back on the menu Home {Y}(y/n){Y}: {G}')

            if Back == 'y' or Back == 'Y':
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if __name__ == '__main__':
                    pyzip()

                elif Back == 'n' or Back == 'N':
                    break

                else:
                    print(f'{please} Sorry! the your Enter Choice Error!{W}')
                    sys.exit()

    except Exception as e:
        print(ERROR(str(e)))

def pyzip():
    def compress_file(file_path):
        os.system('cls' if os.name == 'nt' else 'clear')
        compressed_file_path = f"{file_path}.zip"
        with zipfile.ZipFile(compressed_file_path, 'w') as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        print(f"File compressed: {compressed_file_path}")

    def decompress_file(zip_path):
        output_dir = os.path.dirname(zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            zipf.extractall(output_dir)
        print(f"File decompressed to: {output_dir}")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'''{R}
{R}███████╗     {G}███████╗██╗██████╗     
{R}╚════██║     {G}╚══███╔╝██║██╔══██╗    
{R}    ██╔╝{W}█████╗{G} ███╔╝ ██║██████╔╝    
{R}   ██╔╝ {W}╚════╝{G}███╔╝  ██║██╔═══╝     
{R}   ██║       {G}███████╗██║██║         
{R}   ╚═╝       {G}╚══════╝╚═╝╚═╝                                                                  
{W}''')
        print(f"{G}[1] {B}Compress a file{W}")
        print(f"{G}[2] {B}Decompress a file{W}")
        print(f"{G}[3] {B}Exit{W}")
        choice = input(f"{Enter} Enter your choice: {W}").strip()
        
        if choice == "1":
            file_path = input(f"{Enter} Enter the path of the file to compress: {W}").strip()
            if os.path.isfile(file_path):
                compress_file(file_path)
                Back_Menu()
                break
            else:
                print(f"{please} File does not exist!{W}")

        elif choice == "2":
            zip_path = input(f"{Enter} Enter the path of the zip file to decompress: {Y}").strip()
            if os.path.isfile(zip_path) and zipfile.is_zipfile(zip_path):
                decompress_file(zip_path)
                Back_Menu()
                break

            else:
                print(f"{please} File does not exist or is not a valid zip file!{W}")

        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{other} Exiting...{W}")
            time.sleep(1)
            break

        else:
            print(f"{please} Error choice Please try again!{W}")
            time.sleep(1)
            continue

if __name__ == "__main__":
    pyzip()
