import requests
import time
import sys
import os
from threading import Thread, Lock

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
Working = "\033[94;1m" + '[' + "\033[96;1m" + 'Working' + "\033[94;1m" + ']'
NotWorking = "\033[93;1m" + '[' + "\033[91;1m" + 'Not Working' + "\033[93;1m" + ']' + "\033[91;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
successfully = "\033[93;1m" + "[" + "\033[92;1m" + "successfully" + "\033[93;1m" + "]" + "\033[94;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"
other = "\033[95;1m" + "[" + "\033[93;1m" + "~" + "\033[95;1m" + "]" "\033[92;1m"
notice = Complete = "\033[94;1m" + "[" + "\033[92;1m" + "notice" + "\033[94;1m" + "]" + "\033[92;1m"
Running = "\033[94;1m" + '[Running]' + "\033[95;1m"

stop = False

def Back_Menu():
    try:
        while True:
            Back = input(f'{Question} Do You Go To Back on the menu Home {Y}(y/n){Y}: {G}')

            if Back == 'y' or Back == 'Y':
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if __name__ == '__main__':
                    main()

                elif Back == 'n' or Back == 'N':
                    break

                else:
                    print(f'{please} Sorry! the your Enter Choice Error!{W}')
                    sys.exit()

    except Exception as e:
        print(ERROR(str(e)))

def fetch_proxies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        proxy_ips = []
        for line in response.text.split('\n'):
            parts = line.strip().split(':')
            if len(parts) == 2:
                ip, port = parts
                if ip.count('.') == 3 and port.isdigit():
                    proxy_ips.append(f'{ip}:{port}')

        return proxy_ips

    except requests.exceptions.RequestException as e:
        with Lock():
            print(f'{please} fetching proxies from {url}: {str(e)}{W}')
        return []

def is_proxy_working(proxy):
    try:
        response = requests.get("https://www.example.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        response.raise_for_status()
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        with Lock():
            print(f'{Failed} {proxy} {W}: {NotWorking}{W}')
        return False

def validate_and_print_proxies(proxy_ips, print_limit=None):
    global stop
    working_proxies = set()
    printed_count = 0
    threads = []

    for proxy in proxy_ips:
        if printed_count >= print_limit:
            break

        thread = Thread(target=validate_and_print_proxy, args=(proxy, working_proxies, print_limit))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return working_proxies

def validate_and_print_proxy(proxy, working_proxies, print_limit):
    global stop
    if not stop and is_proxy_working(proxy):
        with Lock():
            if len(working_proxies) < print_limit:
                print(f"{successfully} {proxy} {W}: {Working}{W}")
                working_proxies.add(proxy)

            elif len(working_proxies) >= print_limit:
                stop = True

def save_proxies_to_file(proxies, filename="proxies.txt"):
    with open(filename, "w") as file:
        file.writelines([f"{proxy}\n" for proxy in proxies])

def main():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(rf''' {W}              
  _ __  _ __ _____  ___   _ 
 | '_ \| '__/ {R}_{W} \ \/ / | | |
 | |_) | | | {R}(0){W} >  <| |_| |
 | .__/|_|  \_{R}^{W}_/_/\_\\__, |
 |_|                  |___/ 
''')
        num_proxies_to_print = int(input(f"{Enter} Enter the number of proxies you want to print: {Y}"))
    except ValueError:
        print(f"{please} Error input Please enter agree number!{W}")
        sys.exit(1)

    start_time = time.time()
    
    proxy_urls_HTTP = [
        "https://api.openproxylist.xyz/http.txt",
        "https://alexa.lr2b.com/proxylist.txt",
        "https://rootjazz.com/proxies/proxies.txt",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    ]

    proxy_urls_HTTPS = [
        "https://www.sslproxies.org/",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
    ]

    proxy_urls_SOCKS4 = [
        "https://api.openproxylist.xyz/socks4.txt",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.socks-proxy.net/",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks4/socks4.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
    ]

    proxy_urls_SOCKS5 = [
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://api.openproxylist.xyz/socks5.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/socks5/socks5.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global/socks5_checked.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
        "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    ]

    mixed_url_proxies =  [
        'https://www.sslproxies.org/',
        'https://www.google-proxy.net/',
        'https://free-proxy-list.net/anonymous-proxy.html',
        'https://free-proxy-list.net/uk-proxy.html',
        'https://www.us-proxy.org/',
        'https://free-proxy-list.net/'
    ]

    proxy_urls_MIX = mixed_url_proxies

    print(f"\n{sign} choice the type of proxy: {Y}")
    print(f"{G}[1] {B}HTTP{W}")
    print(f"{G}[2] {B}HTTPS{W}")
    print(f"{G}[3] {B}SOCKS4{W}")
    print(f"{G}[4] {B}SOCKS5{W}")
    print(f"{G}[5] {B}Mixed Proxies (recommended){W}")
    print(f'{G}[6] {B}exit{W}')
    proxy_type = input(f"\n{Enter} Enter your choice: {Y}")

    if proxy_type == "1":
        proxy_urls = proxy_urls_HTTP

    elif proxy_type == "2":
        proxy_urls = proxy_urls_HTTPS

    elif proxy_type == "3":
        proxy_urls = proxy_urls_SOCKS4

    elif proxy_type == "4":
        proxy_urls = proxy_urls_SOCKS5

    elif proxy_type == "5":
        proxy_urls = proxy_urls_MIX
    
    elif proxy_type == '6':
        sys.exit()

    else:
        while True:
            print(f'{ERROR} the choice not Agree !')
            Refresh = input(f'{Question} Do you Try Again Anyway? {Y}(y/n){W}: {Y}')
            if Refresh == 'y' or Refresh == 'Y':
                continue
            elif Refresh == 'n' or Refresh == 'N':
                break
            else:
                sys.exit(0)

    proxy_ips = []

    for url in proxy_urls:
        proxy_ips.extend(fetch_proxies(url))

    working_proxies = validate_and_print_proxies(proxy_ips, print_limit=num_proxies_to_print)

    print(f"\n{sign} List of Working Proxies:\n")
    for proxy in working_proxies:
        print(f"{proxy}")

    save_proxies_to_file(working_proxies)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\n{sign} Time taken: {M}{elapsed_time} {G}seconds{W}")

    current_directory = os.getcwd()
    save_path = os.path.join(current_directory, "proxies.txt")
    print(f"\n{sign} List of Working Proxies saved at: {B}{save_path}{W}")

if __name__ == "__main__":
    main(), Back_Menu()
