import psutil
import os
import time
import keyboard
from datetime import datetime
from prettytable import PrettyTable

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

def background(text, background_color):
    Background_colors = {
        "Black": "\033[40m",
        "Red": "\033[41m",
        "Green": "\033[42m",
        "Yellow": "\033[43m",
        "Blue": "\033[44m",
        "Magenta": "\033[45m",
        "Cyan": "\033[46m",
        "White": "\033[47m",
        "Reset": "\033[0m",
    }
    return f"{Background_colors.get(background_color, Background_colors['Reset'])}{text}{Background_colors['Reset']}"

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

def Banner():
    print(fr'''{R}
    ."""-.
   /      \
   |  _..--'-.
  >.`{W}__.-""\;"`
  / /(     ^\
  '-`)     =|{D}-.
   {W}/{Y}`--.'--'   {D}\ .-.
 {Y}.'`-._ `.\    {D}| J / 
{Y}/      `--.|   {D}\__/ {W}''')
    
def manager_task_system():
    try:
        while True:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            net = psutil.net_io_counters()
            table = PrettyTable()
            print("\033[97;1m")
            table.field_names = [f"{M}ID{W}", f"{G}Resource{W}", f"{B}Value{W}"]
            table.add_row([1, f"{Y}CPU Usage{W}", f"{cpu} {M}%{W}"])
            table.add_row([2, f"{Y}Memory (Total){W}", f"{C}{memory.total / (1024**3):.2f} {Y}GB{W}"])
            table.add_row([3, f"{Y}Memory (Available){W}", f"{C}{memory.available / (1024**3):.2f} {Y}GB{W}"])
            table.add_row([4, f"{Y}Memory (Used){W}", f"{C}{memory.used / (1024**3):.2f} {Y}GB{W}"])
            table.add_row([5, f"{Y}Memory Usage (%){W}", f"{C}{memory.percent} {M}%{W}"])
            table.add_row([6, f"{Y}Disk Space (Total){W}", f"{C}{disk.total / (1024**3):.2f} {Y}GB{W}"])
            table.add_row([7, f"{Y}Disk Space (Used){W}", f"{C}{disk.used / (1024**3):.2f} {Y}GB{W}"])
            table.add_row([8, f"{Y}Disk Space (Free){W}", f"{C}{disk.free / (1024**3):.2f} {Y}GB{W}"])
            table.add_row([9, f"{Y}Disk Space Usage (%){W}", f"{C}{disk.percent} {M}%{W}"])
            table.add_row([10, f"{Y}Bytes Sent{W}", f"{C}{net.bytes_sent / (1024**2):.2f} {Y}MB{W}"])
            table.add_row([11, f"{Y}Bytes Received{W}", f"{C}{net.bytes_recv / (1024**2):.2f} {Y}MB{W}"])
            os.system('cls' if os.name == 'nt' else 'clear')
            Banner()
            print(table)
            DateTime()
            print(f'{sign} for exit press ' + "\033[93;1m" + '[Ctrl + C]' + "\033[97;1m")
            time.sleep(1)
            if keyboard.is_pressed('Ctrl') and keyboard.is_pressed('C'):
                break
    except KeyboardInterrupt:
        print(f'{sign} Exiting using ' + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m")
if __name__ == '__main__':
    manager_task_system()
