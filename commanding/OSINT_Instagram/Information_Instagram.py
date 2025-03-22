import instaloader
import sys
import datetime
import os
from instaloader import Instaloader

def clear_screen():
    current_os = os.name

    if current_os == 'nt':
        os.system('cls')
    elif current_os == 'posix':
        os.system('clear')

clear_screen()

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "[" + "\033[91;1m" + "ERROR" + "\033[93;1m" + "]" + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"

now = datetime.datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")

date_day = "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" + "\033[97;1m" + "(" + "\033[93;1m" + formatted_day + "\033[95;1m" + f" {now:%B %D %Y}" + "\033[97;1m" + ")" + "\033[94;1m" + "[" + "\033[92;1m" + "Time" + "\033[94;1m" + "]" + "\033[93;1m" + "[" + "\033[91;1m" + formatted_time + "\033[93;1m" + "]" + "\033[97;1m"

insta = Instaloader()


def Information_Instagram():
    try:
        print(f'''{Y}
  ___        __                 _           _        
 |_ _|_ __  / _| ___           (_)_ __  ___| |_ __ _ 
  | || '_ \| |_ / _ \   _____  | | '_ \/ __| __/ _` |
  | || | | |  _| (_) | |_____| | | | | \__ \ || (_| |
 |___|_| |_|_|  \___/          |_|_| |_|___/\__\__,_|
                                                     
        {W}''')
        uname = input(f"{Enter} Enter a username: {Y}")
        if uname == "":
            print(f"{Y}[{R}!{Y}] {R}Unknown command!{W}") 
            sys.exit()
        Function = instaloader.Profile.from_username(insta.context, uname)
        print(date_day)
        print(f"{INFO} Username:{W}", Function.username)
        print(f"{INFO} ID:{Y}", Function.userid)
        print(f"{INFO} Full name:{W}", Function.full_name)
        print(f"{INFO} Bio:{B}", Function.biography)
        
        kategori_bisnis_color = f"{Y}None{W}" if Function.business_category_name is None else Function.business_category_name
        print(f"{INFO} Business category name :{B}", kategori_bisnis_color)
        
        url_eksternal_color = f"{Y}None{W}" if Function.external_url is None else Function.external_url
        print(f"{G}[{B}*{G}] {Y}External URL :{G}", url_eksternal_color)

        print(f"{INFO} Followed by people:{W}", f"{R}False{W}" if not Function.followed_by_viewer else f"{G}True{W}")
        print(f"{INFO} Follow:{Y}", Function.followees)
        print(f"{INFO} Followers:{Y}", Function.followers)
        print(f"{INFO} Following people:{W}", f"{R}False{W}" if not Function.follows_viewer else f"{G}True{W}")
        print(f"{INFO} Blocked by people:{W}", f"{R}False{W}" if not Function.blocked_by_viewer else f"{G}True{W}")
        print(f"{INFO} Never blocked anyone:{W}", f"{R}False{W}" if not Function.has_blocked_viewer else f"{G}True{W}")
        print(f"{INFO} Have the spotlight:{W}", f"{G}True{W}" if Function.has_highlight_reels else f"{R}False{W}")
        print(f"{INFO} Have a public story:{W}", f"{Y}None{W}")
        print(f"{INFO} Have asked people:{W}", f"{R}False{W}" if not Function.has_requested_viewer else f"{G}True{W}")
        print(f"{INFO} Requested:{W}", f"{R}False{W}" if not Function.requested_by_viewer else f"{G}True{W}")
        print(f"{INFO} IGTV:{Y}", Function.igtvcount)
        print(f"{INFO} Business account:{W}", f"{R}False{W}" if not Function.is_business_account else f"{G}True{W}")
        print(f"{INFO} Private account:{W}", f"{G}True{W}" if Function.is_private else f"{R}False{W}")
        print(f"{INFO} Verified:{W}", f"{R}False{W}" if not Function.is_verified else f"{G}True{W}")
        print(f"{INFO} Post:{Y}", Function.mediacount)
        print(f"{INFO} Profile photo URL:{W}", f"{Y}None{W}" if not Function.profile_pic_url else f"{G}{Function.profile_pic_url}{W}")

    except KeyboardInterrupt:
        print(f"{sign} completion{W}")

    except EOFError:
        print(f"{ERROR}Why?{W}")
if __name__ == '__main__':
    Information_Instagram()