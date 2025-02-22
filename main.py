import os
import socket
import requests
import wmi
import csv
import re
import random
import keyboard
import string
import sys
import json
import time
import threading
import webbrowser
import wave
import sqlite3
import speedtest
import http.server
import socketserver
import platform
import pkg_resources
import psutil
import pyperclip
import subprocess
import uninstall
from time import sleep
from datetime import datetime
from prettytable import PrettyTable
from termcolor import colored
from colorama import Fore, Style, Back, init; init()
from PyQt5.QtWidgets import (
    QApplication,
      QMainWindow,
        QLabel,
          QLineEdit,
            QPushButton,
              QColorDialog,
                QFileDialog,
                  QMessageBox,
                    QVBoxLayout,
                      QWidget
)
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication
from win10toast import ToastNotifier
from qrcode.image.pil import PilImage
from rich.table import Table
from rich.console import Console
from tqdm import tqdm
from rembg import remove
from PIL import Image
from pathlib import Path
import numpy as np
from commanding import get_pip
from commanding.gaming import XO
from commanding.network import proxy
from commanding.network import chack_network_system
from commanding.system import SystemWinsows
from commanding import WindowsGet
from commanding import zip
from commanding.design.colors import(R, G, B, Y, C, M, W, D, S)
from commanding.design.Terminal import(sign, Enter, ERROR, INFO, Information, Working, NotWorking, warning,
                            Complete, successfully, Failed, please, Question, Help, note, other, 
                            Running, Retrying, Ready, Loading, OK, Okay, stop, Critical, paused,
                            Retrying, Skip, SCAN, Chacking, Hacking, security, AI)
from commanding.design.BackGround import(Red, Green, Blue, Yellow, Cyan, Magenta, White, Black,Dark, Reset)
from commanding import BIOS
from commanding.killer7 import TaskManager
from commanding.OSINT_Instagram import Information_Instagram
from commanding.OSINT_Instagram import find_phone_insta
from commanding import version

def notification():
    try:
        def show_notification(title, message, duration=5):
            toaster = ToastNotifier()
            toaster.show_toast(
            title,
            message,
            duration=duration
        )

        show_notification(
            title="مرحباً بك في Manager Pc",
            message="أتمنى لك وقت ممتع و أستفادة من الخواص الازمة لأجلك و تجربة مريحة.",
            duration=5
        )
    except Exception:
        pass

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

#-----------------------------------------------------------------------------------------------------------------------#
# clear or clean screen terminal

def clear_screen_terminal():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass

#-----------------------------------------------------------------------------------------------------------------------#
# Back to Home 

def Back_Menu():
    try:
        while True:
            Back = input(f'{R}┌─[{M}Mohammed Al-Baqer{Y}@{B}WSL.IQ{R}]─[{G}Do You Go To Back on the menu Home? (y/n){R}]\n└──╼ {R}>{Y}>{G}>{B} ')

            if Back == 'y' or Back == 'Y':
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if __name__ == '__main__':
                    clear_screen_terminal()
                    Banner()
                    table()
                    main()

                elif Back == 'n' or Back == 'N':
                    break

                else:
                    print(f'{please} Sorry! the your Enter Choice Error!{W}')
                    sys.exit()

    except Exception as e:
        print(ERROR(str(e)))
        
#----------------------------------------------------------------------------------------------------------------------#
#noting

def note():
    try:
        while True:
            import sys
            note = "\033[92;1m" + '[' "\033[93;1m" + '*' + "\033[92;1m" + '] ' + "\033[97;1m" + 'Do you want to ' + "\033[92;1m" + 'continue' + "\033[97;1m" + ' or ' + "\033[91;1m" + 'exit' + "\033[97;1m" ' ? ' + "\033[97;1m" + '(' + "\033[92;1m" + "\033[92;1m" + 'c' + "\033[97;1m" + ' , ' + "\033[91;1m" +'e' "\033[97;1m" + '): '
            noting = input(note)
            if note or keyboard.is_pressed('c') or keyboard.is_pressed('continue'):
                continue
            elif noting or keyboard.is_pressed('e') or keyboard.is_pressed('exit'):
                break
            else:
                sys.exit()
    except KeyboardInterrupt:
        pass
        
#-----------------------------------------------------------------------------------------------------------------------#
# Network Traffic Monitoring

def monitor_traffico(intervallo=1, json_filename="network_traffic.json", csv_filename="network_traffic.csv", db_name="network_traffic.db"):
    clear_screen_terminal()
    def convert_bytes(num_bytes):
        if num_bytes < 1024:
            return f"{num_bytes} {B}B{W}"
        elif num_bytes < 1024 ** 2:
            return f"{num_bytes / 1024:.2f} {Y}KB{W}"
        elif num_bytes < 1024 ** 3:
            return f"{num_bytes / (1024 ** 2):.2f} {C}MB{W}"
        else:
            return f"{num_bytes / (1024 ** 3):.2f} {G}GB{W}"

    def setup_database(db_name="network_traffic.db"):
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS traffic (
            id INTEGER PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            interface TEXT,
            bytes_sent INTEGER,
            bytes_recv INTEGER
        )
        ''')
        conn.commit()
        return conn

    def save_to_database(conn, data):
        cursor = conn.cursor()
        for interface, values in data.items():
            cursor.execute('''
            INSERT INTO traffic (interface, bytes_sent, bytes_recv)
            VALUES (?, ?, ?)
            ''', (interface, values['Inviati'], values['Ricevuti']))
        conn.commit()

    def save_to_csv(filename, data):
        file_exists = os.path.isfile(filename)
        with open(filename, mode='a', newline='') as csv_file:
            fieldnames = ['timestamp', 'interface', 'bytes_sent', 'bytes_recv']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            for interface, values in data.items():
                writer.writerow({
                    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'interface': interface,
                    'bytes_sent': values['Inviati'],
                    'bytes_recv': values['Ricevuti']
                })

    conn = setup_database(db_name)
    
    while True:
        stats_iniziali = psutil.net_io_counters(pernic=True)
        time.sleep(intervallo)
        stats_finali = psutil.net_io_counters(pernic=True)
        data = {}

        for interfaccia, stats in stats_finali.items():
            bytes_inviati = stats.bytes_sent - stats_iniziali[interfaccia].bytes_sent
            bytes_ricevuti = stats.bytes_recv - stats_iniziali[interfaccia].bytes_recv
            data[interfaccia] = {
                'Inviati': bytes_inviati,
                'Ricevuti': bytes_ricevuti
            }

        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""
                   {G}\ | /{W}                                                     
                  {B}-- {R}O{B} --{W}                                                    
                    {G}/|\                    
                   {G}/\|/\                 
                  {G}/  |  \                 
                 {G}/\/\|/\/\                    
                {G}/    |    \ 
               -     -     -{W}""")
        
        table = PrettyTable()
        table.field_names = [f"{Y}ID{W}", f"{B}Interfaccia{W}", f"{M}Inviati{W}", f"{G}Ricevuti{W}"]
        
        id_counter = 1
        
        for interfaccia, values in data.items():
            table.add_row([id_counter, M + interfaccia + W, convert_bytes(values['Inviati']), convert_bytes(values['Ricevuti'])])
            id_counter += 1
        
        print(table)
        DateTime()
        print(f'{sign} To exit click {Y}[{R}Ctrl {Y}+ {R}C{Y}]{W}')
        
        save_to_database(conn, data)
        save_to_csv(csv_filename, data)
        
        time.sleep(intervallo)

#-----------------------------------------------------------------------------------------------------------------------#
# psol

def psol():
    clear_screen_terminal()
    print(rf'''
                     {B}. 
                    {B}/ \{W}
  ____  ____        {B}| |{W}
 |  _ \/ ___|  ___  {B}| |{W}  
 | |_) \___ \ / {R}_{W} \ {B}|.|{W}   
 |  __/ ___) | {R}(0){W} |{B}|.|{W}  
 |_|   |____/ \_{R}^{W}_/ {B}|:|{W}  
                    {B}|:|{W}  
                 {W}~{Y}\==8==/{W}~{W}
                     {R}8{W}
                     {R}0{W} 
''')

    def check_tunnel_status(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('serveo.net', 22))
            s.close()
            return f"{B}Online{W}"
        except Exception as e:
            return f"{R}Offline{W}"

    def get_region():
        try:
            response = requests.get("https://ipinfo.io/json")
            data = response.json()
            return data.get('country')
        except Exception as e:
            return "Unknown"

    def generate_web_interface_link(port):
        return f"{G}http://127.0.0.1:{S}{D}{port}{W}"

    def net_port():
        port = input(f"{Enter} Please enter port number: {Y}")
        tunnel_status = check_tunnel_status(port)
        region = get_region()
        web_interface_link = generate_web_interface_link(port)
        command = f"ssh -R 80:localhost:{port} serveo.net"
        print(f"{sign} To stop and exit press {Y}[Ctrl + C]{W}")
        table = PrettyTable()
        table.field_names = [f"{B}ID{W}", f"{G}Services{W}", f"{M}Information{W}"]
        table.add_row([f"{G}1{W}", f"{C}Port{W}", Y + port + W])
        table.add_row([f"{G}2{W}", f"{C}Region{W}", Y + region + W])
        table.add_row([f"{G}3{W}", f"{C}Tunnel Status{W}", tunnel_status + W])
        table.add_row([f"{G}4{W}", f"{C}Web Interface{W}", web_interface_link + W])
        table.add_row([f"{G}5{W}", f"{C}Command{W}", B + command + W])
        print(table)
        DateTime()

        try:
            os.system(command)
        except KeyboardInterrupt:
            sys.exit(0)

    if __name__ == "__main__":
        net_port()

#-----------------------------------------------------------------------------------------------------------------------#
# informations wifi

def get_wifi_info():
    wifi_info = {}
    try:
        c = wmi.WMI()
        for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
            if interface.Description.lower().find('wireless') != -1:
                wifi_info[f'{sign} Adapter name{W}'] = interface.Description
                wifi_info[f'{sign} SSID{W}'] = interface.SettingID
                wifi_info[f'{sign} Connection type{W}'] = f'{Y}N/A{W}'
                wifi_info[f'{sign} IPv4 address{W}'] = interface.IPAddress[0]
                if len(interface.IPAddress) > 1:
                    wifi_info[f'{sign} IPv6 address{W}'] = interface.IPAddress[1]
                else:
                    wifi_info[f'{sign} IPv6 address{W}'] = f'{Y}N/A{W}'
                wifi_info[f'{sign} Manufacturer{W}'] = f'{Y}N/A{W}'
                wifi_info[f'{sign} Description{W}'] = interface.Description
                wifi_info[f'{sign} Driver version{W}'] = f'{Y}N/A{W}'
                wifi_info[f'{sign} Physical address (MAC){W}'] = interface.MACAddress

                netsh_output = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces'], encoding='utf-8')
                ssid_match = re.search(r'^\s*SSID\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                if ssid_match:
                    wifi_info[f'{sign} SSID{W}'] = ssid_match.group(1).strip()

                netsh_output = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=bssid'], encoding='utf-8')
                protocol_match = re.search(r'^\s*Protocol\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                security_type_match = re.search(r'^\s*Authentication\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                network_band_match = re.search(r'^\s*Radio type\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                network_channel_match = re.search(r'^\s*Channel\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                link_speed_match = re.search(r'^\s*Receive rate\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                transmit_speed_match = re.search(r'^\s*Transmit rate\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                ipv4_dns_servers_match = re.search(r'^\s*DNS Servers\s*:\s*(.+)\s*$', netsh_output, re.MULTILINE)
                
                if protocol_match:
                    wifi_info[f'{sign} Protocol{W}'] = protocol_match.group(1).strip()
                if security_type_match:
                    wifi_info[f'{sign} Security type{W}'] = security_type_match.group(1).strip()
                if network_band_match:
                    wifi_info[f'{sign} Network band{W}'] = network_band_match.group(1).strip()
                if network_channel_match:
                    wifi_info[f'{sign} Network channel{W}'] = network_channel_match.group(1).strip()
                if link_speed_match and transmit_speed_match:
                    wifi_info[f'{sign} Link speed (Receive/Transmit){W}'] = f"{link_speed_match.group(1).strip()}/{transmit_speed_match.group(1).strip()} (Mbps)"
                if ipv4_dns_servers_match:
                    wifi_info[f'{sign} IPv4 DNS servers{W}'] = ipv4_dns_servers_match.group(1).strip()
                
                return wifi_info
    except Exception as e:
        pass
    
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'network', 'mode=bssid'], encoding='utf-8')

        ssid_match = re.search(r'^\s*SSID\s*:\s*(.+)\s*$', output, re.MULTILINE)
        protocol_match = re.search(r'^\s*Protocol\s*:\s*(.+)\s*$', output, re.MULTILINE)
        security_type_match = re.search(r'^\s*Authentication\s*:\s*(.+)\s*$', output, re.MULTILINE)
        network_band_match = re.search(r'^\s*Radio type\s*:\s*(.+)\s*$', output, re.MULTILINE)
        network_channel_match = re.search(r'^\s*Channel\s*:\s*(.+)\s*$', output, re.MULTILINE)
        link_speed_match = re.search(r'^\s*Receive rate\s*:\s*(.+)\s*$', output, re.MULTILINE)
        transmit_speed_match = re.search(r'^\s*Transmit rate\s*:\s*(.+)\s*$', output, re.MULTILINE)
        link_local_ipv6_match = re.search(r'^\s*IPv6 Address\s*:\s*(.+)\s*$', output, re.MULTILINE)
        ipv4_match = re.search(r'^\s*IPv4 Address\s*:\s*(.+)\s*$', output, re.MULTILINE)
        ipv4_dns_servers_match = re.search(r'^\s*DNS Servers\s*:\s*(.+)\s*$', output, re.MULTILINE)
        manufacturer_match = re.search(r'^\s*Vendor\s*:\s*(.+)\s*$', output, re.MULTILINE)
        description_match = re.search(r'^\s*Description\s*:\s*(.+)\s*$', output, re.MULTILINE)
        driver_version_match = re.search(r'^\s*Driver version\s*:\s*(.+)\s*$', output, re.MULTILINE)
        mac_address_match = re.search(r'^\s*Physical address\s*:\s*(.+)\s*$', output, re.MULTILINE)

        if ssid_match:
            wifi_info[f'{sign} SSID{W}'] = ssid_match.group(1).strip()
        if protocol_match:
            wifi_info[f'{sign} Protocol{W}'] = protocol_match.group(1).strip()
        if security_type_match:
            wifi_info[f'{sign} Security type{W}'] = security_type_match.group(1).strip()
        if network_band_match:
            wifi_info[f'{sign} Network band{W}'] = network_band_match.group(1).strip()
        if network_channel_match:
            wifi_info[f'{sign} Network channel{W}'] = network_channel_match.group(1).strip()
        if link_speed_match and transmit_speed_match:
            wifi_info[f'{sign} Link speed (Receive/Transmit){W}'] = f"{link_speed_match.group(1).strip()}/{transmit_speed_match.group(1).strip()} (Mbps)"
        if link_local_ipv6_match:
            wifi_info[f'{sign} Link-local IPv6 address{W}'] = link_local_ipv6_match.group(1).strip()
        if ipv4_match:
            wifi_info[f'{sign} IPv4 address{W}'] = ipv4_match.group(1).strip()
        if ipv4_dns_servers_match:
            wifi_info[f'{sign} IPv4 DNS servers{W}'] = ipv4_dns_servers_match.group(1).strip()
        if manufacturer_match:
            wifi_info[f'{sign} Manufacturer{W}'] = manufacturer_match.group(1).strip()
        if description_match:
            wifi_info[f'{sign} Description{W}'] = description_match.group(1).strip()
        if driver_version_match:
            wifi_info[f'{sign} Driver version{W}'] = driver_version_match.group(1).strip()
        if mac_address_match:
            wifi_info[f'{sign} Physical address (MAC){W}'] = mac_address_match.group(1).strip()
        
        return wifi_info
    except subprocess.CalledProcessError:
        return {"Error": "Failed to retrieve WiFi information"}

#-----------------------------------------------------------------------------------------------------------------------#        
# show password network

def show_password_network():
    clear_screen_terminal()
    print(fr'''{R}
    ."""-.
   /      \
   |  _..--'-.
  >.`{W}__.-""\;"`
  / /(     ^\
  '-`)     =|{D}-.
   {W}/{Y}`--.'--'   {D}\ .-.
 {Y}.'`-._ `.\    {D}| J / 
{Y}/      `--.|   {D}\__/ {W}
 __ _                       ___
/ _\ |__   _____      __   / _ \__ _ ___ ___
\ \| '_ \ / {R}_{W} \ \ /\ / /  / /_)/ _` / __/ __|
_\ \ | | | {R}(0){W} \ V  V /  / ___/ (_| \__ \__ \
\__/_| |_|\_{R}^{W}_/ \_/\_/   \/    \__,_|___/___/
    ''')
    table = PrettyTable()
    table.field_names = [f"{B}ID{W}", f"{M}Name{W}", f"{Y}Password{W}"]
    networks = os.popen('netsh wlan show profile').read()
    network_names = []

    for line in networks.split('\n'):
        if "All User Profile" in line:
            name = line.split(":")[1].strip()
            network_names.append(name)
    
    for idx, name in enumerate(network_names, 1):
        network_details = os.popen(f'netsh wlan show profile name="{name}" key=clear').read()
        password_line = [line for line in network_details.split('\n') if "Key Content" in line]
        password = password_line[0].split(":")[1].strip() if password_line else "None"        
        table.add_row([idx, name, password])
    
    print(table)

#-----------------------------------------------------------------------------------------------------------------------#
# WSL

def wsl():
    try:
        clear_screen_terminal()
        if os.name != 'nt':
            print("This script is designed for Windows only.")
            return
        print(fr"""
            {W}•{B}_{W}•      
            {Back.YELLOW}oo{S}{B}|          
           / '\'        
          {Back.YELLOW}({S}{B}\_;/{Back.YELLOW}){S}{B}            
     _ _ _ _____ __    
    | | | |   __|  |   
    | | | |__   |  |__ 
    |_____|_____|_____|{W}""")
        print(f'\n{Back.RED} Windows Subsystem for Linux {S}{W}\n')
        print(f"{G}[1] {B}Activate (WSL){W}")
        subprocess.run("wsl --install", shell=True, check=True)
        print(f"\n{G}[2] {B}View list of distributions (wsl){W}")
        result = subprocess.run("wsl --list --online", shell=True, text=True, capture_output=True)
        print(result.stdout)
        print(f"\n{G}[3] {B}Enter the name of the distribution you want to install Frol (wsl):{W}")
        distro = input(f"{Y}>{W} ").strip()
        print(f"{sign} Installing distribution {W}'{distro}'...")
        subprocess.run(f"wsl --install -d {distro}", shell=True, check=True)
        print(f"\n{sign} Opening a webpage for the selected distribution's environment...{W}")
        distro_links = {
            "Ubuntu": "https://ubuntu.com/wsl",
            "Debian": "https://www.debian.org/",
            "Kali": "https://www.kali.org/",
            "Fedora": "https://getfedora.org/",
            "OpenSUSE": "https://en.opensuse.org/",
            "Alpine": "https://alpinelinux.org/"
        }
        
        if distro in distro_links:
            webbrowser.open(distro_links[distro])
            print(f"{sign} Opened link: {W}{distro_links[distro]}")

        else:
            print(f"{please} No link found for this distribution. Please search manually!{W}")
        print(f"\n{INFO} WSL and your chosen distribution were successfully installed.{W}")

    except subprocess.CalledProcessError as e:
        print(f"{please}An error occurred while executing a command: {e}{W}")

    except Exception as e:
        print(f"{please} An unexpected error occurred: {e}{W}")

#-----------------------------------------------------------------------------------------------------------------------#
# uninstall wsl

def uninstall_wsl():
    remove_wsl = input(f"{Enter} Do you want to uninstall WSL? {Y}(y/n){B}: {Y}").strip().lower()
    
    if remove_wsl == 'y':
        commands = [
            "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force",
            r"commanding\UninstallWSL.ps1"
        ]

        for command in commands:
            try:
                result = subprocess.run(
                    ["powershell", "-Command", command],
                    capture_output=True,
                    text=True,       
                    check=True
                )
                print(f"Command executed successfully: {command}")
                print(f"Output:\n{result.stdout}")

            except subprocess.CalledProcessError as e:
                print(f"{Failed} Error executing command: {command}")
                print(f"{Failed} Error message:\n{e.stderr}")

    elif remove_wsl == 'n':
        print(f'{sign} Exit...{W}')
        sys.exit()

    else:
        print(f"{ERROR} input Please enter 'y' or 'n'!{W}")

#-----------------------------------------------------------------------------------------------------------------------#
# control folder show and hide for folder

def folder():

    def log_change(action, folder_path):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("history.txt", "a") as file:
            print(f'{sign} Save to file complete {Y}[{B}history.txt{Y}]{W}')
            file.write(f"{current_time} - {action}: {folder_path}\n")

    def Show_Hide():
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                console = Console()
                table = Table(title="Show & Hide folders")
                table.add_column("ID", justify="right", style="cyan", no_wrap=True)
                table.add_column("Tool", style="magenta")

                table.add_row("1", "Hide folder")
                table.add_row("2", "Show folder")
                console.print(table)
            
                choice = input(f'{Enter} Enter Choice number: {Y}')
                if choice == '1':
                    Hide = input(f'{Enter} Enter folder path to hide: {Y}')
                    DateTime()
                    Hide = Hide.strip("'").strip('"')
                    os.system(rf'attrib +h +s "{Hide}"')
                    log_change("Hide", Hide)
                    break
                elif choice == '2':
                    Show = input(f'{Enter} Enter folder path to show: {Y}')
                    DateTime()
                    Show = Show.strip("'").strip('"')
                    os.system(rf'attrib -h -s "{Show}"')
                    log_change("Show", Show)
                    break
                else:
                    print(f'{ERROR} False choice. Please enter 1 or 2!{W}')
        except Exception as e:
            print(f"Error: {str(e)}")

    if __name__ == "__main__":
        Show_Hide()

#-----------------------------------------------------------------------------------------------------------------------#
# generate for password

def passwords():
    def generate_password(Length):
        uppercase_chars = string.ascii_uppercase
        Lowrcase_chars = string.ascii_lowercase
        number_chars = string.digits
        special_chare = string.punctuation

        possible_chare = uppercase_chars + Lowrcase_chars + number_chars + special_chare

        Length = max(Length, 8)
        password = ''.join(random.choice(possible_chare) for i in range(Length))
    
        with open('passwords.txt', 'a') as f:
            print(f'{sign} Save to file complete {Y}[{B}passwords.txt{Y}]{W}')
            f.write(password + '\n')
        return password

    try:
        user_length = int(input(f"{Enter} Enter the password length {Y}(minimum 8):{M} "))
        if user_length < 8:
            print(f"{sign} The length is set to 8 as it is the minimum.{W}")
        password = generate_password(user_length)
        print(f"{sign} Generated password:{M} {password}")
    except ValueError:
        print(f"{please} Please enter a valid number!{W}")

#-----------------------------------------------------------------------------------------------------------------------#
# Encrypt and Decrypt images audio and binary

def Encrypt_decrypt_images_audio_binary():
    os.system('cls' if os.name == 'nt' else 'clear')
    def encrypt_image_to_binary(image_path, binary_file):
        image_path = image_path.strip("'").strip('"')
        binary_file = binary_file if binary_file.endswith(".bin") else binary_file + ".bin"
        try:
            image = Image.open(image_path).convert("RGB")
            pixels = np.array(image)
            with open(binary_file, "wb") as f:
                np.save(f, pixels)
            print(f"{sign} Image encrypted to binary file: {Y}{binary_file}")
        except Exception as e:
            print(str(e))

    def encrypt_image_to_audio(image_path, audio_file):
        image_path = image_path.strip("'").strip('"')
        audio_file = audio_file if audio_file.endswith(".wav") else audio_file + ".wav"
        try:
            image = Image.open(image_path).convert("RGB")
            pixels = np.array(image)
            flat_pixels = pixels.flatten()
            normalized_data = (flat_pixels / 255.0 * 32767).astype(np.int16)

            with wave.open(audio_file, "w") as audio:
                audio.setnchannels(1) 
                audio.setsampwidth(2)  
                audio.setframerate(44100)
                audio.writeframes(normalized_data.tobytes())
            print(f"{sign} Image encrypted to audio file:{Y} {audio_file}")
        except Exception as e:
            print(str(e))

    def decrypt_binary_to_image(binary_file, output_image):
        binary_file = binary_file.strip("'").strip('"')
        output_image = output_image if output_image.lower().endswith((".png", ".jpg", ".jpeg")) else output_image + ".png"
        try:
            with open(binary_file, "rb") as f:
                pixels = np.load(f)
            image = Image.fromarray(pixels.astype("uint8"))
            image.save(output_image)
            print(f"{sign} Binary file decrypted to image:{Y} {output_image}")
        except Exception as e:
            print(str(e))

    def decrypt_audio_to_image(audio_file, output_image):
        audio_file = audio_file.strip("'").strip('"')
        output_image = output_image if output_image.lower().endswith((".png", ".jpg", ".jpeg")) else output_image + ".png"
    
        try:
            with wave.open(audio_file, "r") as audio:
                frames = audio.readframes(audio.getnframes())
                data = np.frombuffer(frames, dtype=np.int16)
        
            total_pixels = len(data)
            side_length = int(np.sqrt(total_pixels / 3))
            original_shape = (side_length, side_length, 3)

            normalized_data = (data / 32767.0 * 255).astype(np.uint8)
            pixels = normalized_data.reshape(original_shape)
        
            image = Image.fromarray(pixels)
            image.save(output_image)
            print(f"{sign} Audio file decrypted to image:{Y} {output_image}")
    
        except Exception as e:
            print(str(e))

    def main():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            console = Console()
            table = Table(title="Menu")
            table.add_column("ID", justify="right", style="cyan", no_wrap=True)
            table.add_column("Tool", style="magenta")

            table.add_row("1", "Encrypt Image")
            table.add_row("2", "Decrypt Image")
            table.add_row("3", "Exit")
            console.print(table)

            choice = input(f"{Enter} Choose an option: {Y}").strip()
            if choice == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                console = Console()
                table = Table(title="Encrypt Image")
                table.add_column("ID", justify="right", style="cyan", no_wrap=True)
                table.add_column("option", style="magenta")

                table.add_row("1", "Encrypt to Binary File")
                table.add_row("2", "Encrypt to Audio File")
                console.print(table)
          
                encrypt_choice = input(f"{Enter}Choose an encryption method: {Y}").strip()

                image_path = input(f"{Enter} Enter the path to the image: {Y}").strip()
                if encrypt_choice == "1":
                    binary_file = input(f"{Enter} Enter the name for the binary file (e.g., output): {Y}").strip()
                    encrypt_image_to_binary(image_path, binary_file)
                elif encrypt_choice == "2":
                    audio_file = input(f"{Enter} Enter the name for the audio file (e.g., output): {Y}").strip()
                    encrypt_image_to_audio(image_path, audio_file)
                else:
                    print(f"{please} Error option!{W}")

            elif choice == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                console = Console()
                table = Table(title="Decrypt Options")
                table.add_column("ID", justify="right", style="cyan", no_wrap=True)
                table.add_column("option", style="magenta")

                table.add_row("1", "Decrypt from Binary File")
                table.add_row("2", "Decrypt from Audio File")
                console.print(table)

                decrypt_choice = input(f"{Enter} Choose a decryption method: {Y}").strip()

                if decrypt_choice == "1":
                    binary_file = input(f"{Enter} Enter the binary file path: {Y}").strip()
                    output_image = input(f"{Enter} Enter the name for the output image (e.g., output): {Y}").strip()
                    decrypt_binary_to_image(binary_file, output_image)
                elif decrypt_choice == "2":
                    audio_file = input(f"{Enter} Enter the audio file path: {Y}").strip()
                    output_image = input(f"Enter the name for the output image (e.g., output): {Y}").strip()
                    decrypt_audio_to_image(audio_file, output_image)
                else:
                    print(f"{please} Error option!{Y}")

            elif choice == "3":
                print(f"{other} Exiting...{Y}")
                break
            else:
                print(f"{please} Error option!{W}")

    if __name__ == "__main__":
        main()

#-----------------------------------------------------------------------------------------------------------------------#
# istp

def istp():

    def Banner_istp():
        print(f"""
      {G}\ | /{W}                                                     
     {B}-- {R}O{B} --{W}                                                    
       {G}/|\       {B} ___  ____________________________{W}             
      {G}/\|/\      {B}|   |/   _____/__    ___/______   \{W}            
     {G}/  |  \     {B}|   |\_____  \  |    |   |     ___/{W}            
    {G}/\/\|/\/\    {B}|   |/        \ |    |   |    |{W}                
   {G}/    |    \   {B}|___|_______  / |____|   |____| {Y}Version : Professional{W}
  -     -     -        {B}      \/{W}                  {Y}By {W}: Mohammed Al-Baqer{M}{W}          
 {Back.RED}{W} [Internet Speed Test Ping] {S}{W}""")

    def clear_screen():
        operating_system = os.name
        try:
            if (operating_system == 'posix'):
                os.system('clear')
            elif (operating_system == 'nt'):
                os.system('cls')
            else:
                print(f"{please} System unknown!{S}")
        except Exception as e:
            print(f"{ERROR}{W}: {e}")

    clear_screen()

    def spin():
        delay = 0.25
        spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

        for _ in range(1):
            for i in spinner:
                message = f"[*] {B}Checking your internet connection...[{i}]{W}"
                colored_message = colored(message, 'blue', attrs=['bold'])
                sys.stdout.write(f"\r{colored_message}   ")
                sys.stdout.flush()
                time.sleep(delay)

        sys.stdout.write("\r")
        sys.stdout.flush()
        done_message = colored("[+] Your Internet connection has been verified", 'yellow', attrs=['bold'])
        sys.stdout.write("\033[K")
        print(done_message)
        time.sleep(1)
    spin()

    def check_internet_connection():
        try:
            response = requests.get('http://www.google.com', timeout=5)
            return True
        except requests.ConnectionError:
            return False

    if check_internet_connection():
        print(f"{sign} Internet connection is available. You can proceed with execution.{W}")
        time.sleep(0.25)
    else:
        print(f"{please} No internet connection !{W}")
        exit()

    clear_screen()
    Banner_istp()
    print("\033[0m") # Reset color
    print(f"{INFO} system is {W}: {B}Windows{W}")
    wifi_info = get_wifi_info()
    for key, value in wifi_info.items():
        print(f"{key}: {value}")

    input(f"{Enter} {Help}{W}")
    init(autoreset=True)
    print(f"{sign} {Y}Downloading to servers and information at internet speed.{W}")

    def show_loading():
        spinner = [f'{R}-{W}', f'{G}\\{W}', f'{B}|{W}', f'{Y}/{W}']
        index = 0
        while not stop_loading:
            print(f"{sign}{W} Please waiting {spinner[index]}", end='\r', flush=True)
            index = (index + 1) % len(spinner)
            time.sleep(0.2)

    def main_task():
        global stop_loading
        stop_loading = False
        loading_thread = threading.Thread(target=show_loading)
        loading_thread.start()
        st = speedtest.Speedtest()
        st.get_best_server()
        stop_loading = True
        loading_thread.join()
        sys.stdout.write("\r\033[K")
        DateTime()
        for _ in tqdm(range(10), colour="green", desc=f"{INFO} Finding  Optimal  Server"):
            sleep(0.05)

        st.download()
        for _ in tqdm(range(10), colour="yellow", desc=f"{INFO} Getting {W}[{Y}Download{W}] {M}Speed"):
            sleep(0.05)

        st.upload()
        for _ in tqdm(range(10), colour="red", desc=f"{INFO} Getting  {W}[{Y}Upload{W}] {M} Speed"):
            sleep(0.05)

        res_dict = st.results.dict()

        dwnl = f"{res_dict['download'] / 10**6:.2f}"
        upl = f"{res_dict['upload'] / 10**6:.2f}"
        print(W)
        table = PrettyTable()
        table.field_names = [f"{M}ID{W}", f"{B}INFORMATION{W}", f"{R}Information results{W}"]
        table.add_row([f"{G}1{W}", f"{Y}Download{W}", f"{B}{dwnl} {M}Mbps{W} ({B}{float(dwnl) * 0.125:.2f} {G}MB/s{W})"])
        table.add_row([f"{G}2{W}", f"{Y}Upload{W}", f"{B}{upl} {M}Mbps{W} ({B}{float(upl) * 0.125:.2f} {G}MB/s{W})"])
        table.add_row([f"{G}3{W}", f"{Y}Ping{W}", f"{B}{res_dict['ping']:.2f} {G}ms{W}"])
        table.add_row([f"{G}4{W}", f"{Y}HOST{W}", res_dict['server']['host']])
        table.add_row([f"{G}5{W}", f"{Y}SPONSOR{W}", res_dict['server']['sponsor']])
        table.add_row([f"{G}6{W}", f"{Y}ISP{W}", res_dict['client']['isp']])
        table.add_row([f"{G}7{W}", f"{Y}Country{W}", res_dict['client']['country']])
        table.add_row([f"{G}8{W}", f"{Y}URL{W}", st.results.share()])
        table.add_row([f"{G}9{W}", f"{Y}Hosted By{W}", res_dict['server']['host']])
        packet_loss = res_dict.get('packetLoss', 'N/A')
        table.add_row([f"{G}10{W}", f"{Y}Packet Loss{W}", f"{B}{packet_loss}%{W}"])
        table.add_row([f"{G}11{W}", f"{Y}Server ID{W}", res_dict['server']['id']])
        table.add_row([f"{G}12{W}", f"{Y}ISP Rating{W}", res_dict['client']['isprating']])
        print(table)
        DateTime()

        while True:
            tracking = input(f'{Question} Do you Network Traffic Monitoring {Y}(y/n){W}: ')
            if tracking == 'y' or tracking == 'Y':
                monitor_traffico()
                break
            elif tracking == 'n' or tracking == 'N':
                for i in range(1, 101):
                    print(f'[{i}%] Loading to exit')
                    time.sleep(0.01)
                    os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                continue

    main_task()

#-----------------------------------------------------------------------------------------------------------------------#
# server speed test

def server_st():

    def Banner():
        operating_system = os.name
        try:
            if (operating_system == 'posix'):
                os.system('clear')
            elif (operating_system == 'nt'):
                os.system('cls')
            else:
                print(f"{please} System unknown!{S}")
        except Exception as e:
            print(f"{ERROR}{W}: {e}")

        print(rf"""{Y}
 __            ___              
|__| ____   __| _/ ____ ___  ___
|  |/    \ / __ |_/ __ \\  \/  /
|  |   |  \ /_/ |\  ___/_\    / 
|__|___|  /____ | \___  /__/\_ \
        \/     \/     \/      \/
    """)
    #datatime
    Banner()

    Localhost = '127.0.0.1'
    Port = 8000

    def slowprint(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.05)

    slowprint(f"{B}$ {G}index.html{W}\r\n")

    FILENAME = "index.html"

    class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = FILENAME
            return super().do_GET()

    os.chdir('server')

    handler_object = CustomHTTPRequestHandler

    def run_server():
       with socketserver.TCPServer(("", Port), handler_object) as httpd:
            print(f"{INFO} Serving at port {G}{Port}{W}")
            httpd.serve_forever()

    print(f'{B}$ {G}http://{Localhost}{W}:{Y}{Port}{W}')

    def open_browser():
        webbrowser.open(f"http://localhost:{Port}")

    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    open_browser()

#-----------------------------------------------------------------------------------------------------------------------#
# Python Executable

def Python_Executable():
    def py_exe():
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{G}                                                         
 _____     _   _              _____                 _       _   _     
|  _  |_ _| |_| |_ ___ ___   |   __|_ _ ___ ___ _ _| |_ ___| |_| |___ 
|   __| | |  _|   | . |   |  |   __|_'_| -_|  _| | |  _| .'| . | | -_|
|__|  |_  |_| |_|_|___|_|_|  |_____|_,_|___|___|___|_| |__,|___|_|___|
      |___|                                                           {W}\n""")
            print(background(f"{W} Python Executable Convert code from (.py) to (.exe) ", "Yellow"))
            desktop_path = Path.home() / 'Desktop'
            while True:
                print(f"{G}[1]{B} Single file{W}")
                print(f"{G}[2]{B} Folder containing a project{W}")
                choice = input(f"{Y}Select the source type (1/2): {S}").strip()

                if choice == "1":
                    source_path = input(f"{Enter} Enter the Python file name (.py): {S}").strip()
                    if not os.path.isfile(source_path):
                        print(f"{please} The file does not exist. Please try again!{W}")
                        continue
                    main_script = source_path

                elif choice == "2":
                    folder_path = input(f"{Enter} Enter the folder path: {Y}").strip()
                    if not os.path.isdir(folder_path):
                        print(f"{please} The folder does not exist. Please try again!{W}")
                        continue
                    print(f"{sign} Python files in the folder:{W}")
                    py_files = [f for f in os.listdir(folder_path) if f.endswith(".py")]

                    for i, file in enumerate(py_files, 1):
                        print(f"{G}{i}.{W} {file}")

                    if not py_files:
                        print(f"{ERROR} No Python files found in the folder!{S}")
                        continue

                    main_index = int(input(f"{Enter} Select the main file (number): {W}")) - 1
                    main_script = os.path.join(folder_path, py_files[main_index])

                else:
                    print(f"{please} False choice Please try again!{W}")
                    continue

                icon_choice = input(f"{Question} Do you want to add an icon? (y/n): {Y}").lower()
                icon_option = ""

                if icon_choice == "y":
                    icon_path = input(f"{Enter} Enter the path to the .ico file: {Y}").strip()
                    if os.path.isfile(icon_path):
                        icon_option = f'--icon="{icon_path}"'

                    else:
                         print(f"{please} False icon path. It will be skipped!{W}")

                console_choice = input(f"{Question} Do you want to hide the console window? (y/n): {W}").lower()
                console_option = "--windowed" if console_choice == "y" else ""
                command = rf'pyinstaller --onefile {icon_option} {console_option} --distpath "{desktop_path}" "{main_script}"'
                print(f"{sign} Executing the following command:{W}\n{B}{command}{W}")
                os.system(command)
                print(f"{sign} The executable file has been created on the desktop!{W}")
                break

        except Exception as e:
            print(ERROR(str(e)))
    py_exe()

#-----------------------------------------------------------------------------------------------------------------------#
# Python Package Manager

def python_package_manager():
    def clearScreen():
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print('Error: ' + str(e))

    def slowprint(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01)

    def display_python_environment_info():
        print(f"{G}===== {Y}Python Environment Information {G}====={W}")
        print(f"{sign} Python Version:", platform.python_version())
        print(f"{sign} Python Implementation:", platform.python_implementation())
        print(f"{sign} Python Compiler:", platform.python_compiler())
        print(f"{sign} Python Build:", platform.python_build())
        print(f"\n{G}===== {M}Operating System Information {G}====={W}")
        print(f"{sign} System:", platform.system())
        print(f"{sign} Node Name:", platform.node())
        print(f"{sign} Release:", platform.release())
        print(f"{sign} Version:", platform.version())
        print(f"{sign} Machine:", platform.machine())
        print(f"{sign} Processor:", platform.processor())
        print(f"\n{B}===== {Y}Python Path {B}====={M}")
        for path in sys.path:
            print(path)
        print(f"\n{R}===== {G}Installed Packages {R}====={W}")
        installed_packages = sorted([(d.project_name, d.version) for d in pkg_resources.working_set])
        for package_name, version in installed_packages:
            print(f"{B}=> {G}{package_name}{Y}=={R}{version}{W}")

    def install_package_version():
        library_name = input(f"{Enter} Enter the library name: {Y}")
        version = input(f"{Enter} Enter the version number: {Y}")
        slowprint(f"{D}$ {B}pip install {G}{library_name}{Y}=={R}{version}{W}\n")
        os.system(f"pip install {library_name}=={version}")
        print(f"Attempted to install {G}{library_name} version {R}{version}.")

    def Developer(text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.01)

    def loading_animation():
        loading_symbols = [f'{R}|', f'{G}/', f'{B}-', f'{Y}\\']
        print("Loading...", end=" ", flush=True)
        for i in range(20):
            symbol = loading_symbols[i % len(loading_symbols)]
            print(f'\rLoading... {symbol}', end='', flush=True)
            time.sleep(0.09)

    # Main logic
    try:
        while True:
            clearScreen()
            print(f'''{M}                                                                                
 _____     _   _              _____         _               
|  _  |_ _| |_| |_ ___ ___   |  _  |___ ___| |_ ___ ___ ___ 
|   __| | |  _|   | . |   |  |   __| .'|  _| '_| .'| . | -_|
|__|  |_  |_| |_|_|___|_|_|  |__|  |__,|___|_,_|__,|_  |___|
      |___|                                        |___|  
           {G}By {W}: {B}Mohammed Al-Baqer                  
{W}''')
            Developer(f'{B}[{G}Python packages{B}]{W} were developed by {R}[{Y}Mohammed Al-Baqer{R}]{W}\n\n')
            text = ['show list of installed pip packages', 'install a pip package', 'uninstall a pip package', 'upgrade pip', 'Update a specific package', 'show informations for python and version', 'installpackage and version', 'About Developer', 'exit']

            for i, command in enumerate(text, start=1):
                print(f'{Y}[{i}] {B}{command}{S}')
            choice = input(f'\n{Enter} Enter choice number: {W}')

            if choice == '1':
                loading_animation()
                clearScreen()
                os.system('pip list')

            elif choice == '2':
                install = input(f'{Enter} Enter package name to install: {W}')
                os.system(f'pip install {install}')

            elif choice == '3':
                clearScreen()
                print(W)
                os.system('pip list')
                uninstall = input(f'\n{Enter} Enter package name from list to uninstall: {W}')
                os.system(f'pip uninstall {uninstall} -y')

            elif choice == '4':
                clearScreen()
                print(W)
                os.system('python -m pip install --upgrade pip')

            elif choice == '5':
                clearScreen()
                print(W)
                os.system('pip list')
                pkg = input(f'\n{Enter} Enter name package for upgrade: {W}')
                os.system(f'pip install --upgrade {pkg}')

            elif choice == '6':
                clearScreen()
                print(W)
                display_python_environment_info()
                print(f"\n{Y}===== {M}Informations color {Y}====={W}")
                print(f'{G}━━━━━━━ package name')
                print(f'{R}━━━━━━━ package version')

            elif choice == '7':
                clearScreen()
                print(W)
                install_package_version()

            elif choice == '8':
                clearScreen()
                slowprint(f'{C}Welcome.\n{G}Good greet from the Developer.{W}\nMy name is {Y}Mohammed Al-Baqer{W} Developer and Programmed by using {B}Python Programming language.{W}\nThis program is your guide to help in {B}Python language{W} but in ashort and simple.\nTo report or help continue through.\n{R}Telegram {Y}=> {B}@R94XS{G}\nThank You for using the program.\nI wish You a good time.\n')

            elif choice == '9':
                print(f'{G}Exiting...{S}')
                break

            else:
                print(f'{please} Error choice Please try again!{W}')
                sys.exit(0)
            input(f'\n{Enter} {Help}{S}')
            clearScreen()

    except Exception as e:
        print(f'{please} Error: ' + str(e))

#-----------------------------------------------------------------------------------------------------------------------#
# password GUI

class PasswordGeneratorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("توليد كلمات سر عشوائية")
        self.setMinimumSize(400, 300)
        self.setGeometry(100, 100, 600, 400)        
        self.uppercase = True
        self.lowercase = True
        self.numbers = True
        self.symbols = True
        self.length = 12
        layout = QtWidgets.QVBoxLayout()
        self.logo_label = QtWidgets.QLabel()
        self.logo_label.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.logo_label)
        self.label_title = QtWidgets.QLabel("توليد كلمات سر عشوائية")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label_title)
        checkbox_layout = QtWidgets.QHBoxLayout()
        self.uppercase_checkbox = QtWidgets.QCheckBox("ABXY")
        self.uppercase_checkbox.setChecked(True)
        self.uppercase_checkbox.stateChanged.connect(self.update_charset)
        checkbox_layout.addWidget(self.uppercase_checkbox)
        self.lowercase_checkbox = QtWidgets.QCheckBox("abxy")
        self.lowercase_checkbox.setChecked(True)
        self.lowercase_checkbox.stateChanged.connect(self.update_charset)
        checkbox_layout.addWidget(self.lowercase_checkbox)
        self.numbers_checkbox = QtWidgets.QCheckBox("123")
        self.numbers_checkbox.setChecked(True)
        self.numbers_checkbox.stateChanged.connect(self.update_charset)
        checkbox_layout.addWidget(self.numbers_checkbox)
        self.symbols_checkbox = QtWidgets.QCheckBox("!@#$%^&*")
        self.symbols_checkbox.setChecked(True)
        self.symbols_checkbox.stateChanged.connect(self.update_charset)
        checkbox_layout.addWidget(self.symbols_checkbox)     
        layout.addLayout(checkbox_layout)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(4)
        self.slider.setMaximum(50)
        self.slider.setValue(12)
        self.slider.valueChanged.connect(self.update_length)
        layout.addWidget(self.slider)
        self.label_length = QtWidgets.QLabel(f"طول كلمة السر: {self.length}")
        self.label_length.setAlignment(QtCore.Qt.AlignCenter)
        layout.addWidget(self.label_length)
        self.password_display = QtWidgets.QLabel("هنا كلمة المرور الخاصة بك")
        self.password_display.setAlignment(QtCore.Qt.AlignCenter)
        self.password_display.setStyleSheet("background-color: white; font-size: 16px; padding: 10px;")
        layout.addWidget(self.password_display)
        button_layout = QtWidgets.QHBoxLayout()
        self.generate_button = QtWidgets.QPushButton("أنشاء كلمة سر")
        self.generate_button.clicked.connect(self.generate_password)
        self.generate_button.setStyleSheet("background-color: #4CAF50; color: white;")
        button_layout.addWidget(self.generate_button)
        self.copy_button = QtWidgets.QPushButton("نسخ كلمة المرور")
        self.copy_button.clicked.connect(self.copy_password)
        self.copy_button.setStyleSheet("background-color: #2196F3; color: white;")
        button_layout.addWidget(self.copy_button)   
        self.about_button = QtWidgets.QPushButton("حول المطور")
        self.about_button.clicked.connect(self.show_about)
        self.about_button.setStyleSheet("background-color: #f44336; color: white;")
        button_layout.addWidget(self.about_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def update_charset(self):
        self.uppercase = self.uppercase_checkbox.isChecked()
        self.lowercase = self.lowercase_checkbox.isChecked()
        self.numbers = self.numbers_checkbox.isChecked()
        self.symbols = self.symbols_checkbox.isChecked()

    def update_length(self, value):
        self.length = value
        self.label_length.setText(f"طول كلمة السر: {self.length}")
        if value <= 8:
            self.slider.setStyleSheet("QSlider::handle:horizontal {background: red;}")
        elif 8 < value <= 12:
            self.slider.setStyleSheet("QSlider::handle:horizontal {background: yellow;}")
        else:
            self.slider.setStyleSheet("QSlider::handle:horizontal {background: green;}")

    def generate_password(self):
        charset = ""
        if self.uppercase:
            charset += "QWERTYUIOPASDFGHJKLZXCVBNM"

        if self.lowercase:
            charset += "qwertyuiopasdfghjklzxcvbnm"

        if self.numbers:
            charset += "1234567890"

        if self.symbols:
            charset += "!@#$%^&*"

        if charset:
            password = "".join(random.choice(charset) for _ in range(self.length))
            self.password_display.setText(password)

        else:
            self.password_display.setText("لا يمكن أنشاء كلمة سر بدون تحديد نوع الرمز الرجاء تحديد نوع")

    def copy_password(self):
        pyperclip.copy(self.password_display.text())
        QtWidgets.QMessageBox.information(self, "تم النسخ", "تم نسخ كلمة المرور الخاصة بك")

    def show_about(self):
        QtWidgets.QMessageBox.information(self, "حول المطور", """* تم برمجة و تطوير هذا البرنامج بواسطة (مـحمد البــاقـر)
- تم أنشاءهُ بواسطة لغة Python ضمن أطار العمل بمكتبة PyQt5 
- أسعىٰ إن يكون البرنامج يســاعدك 
علىٰ توليد ڪلمات سر لتأمين بها خصوصيتك
- شڪراً علىٰ أستخدامك للبرنامج -

Developer: Mohammed AL-Baqer""")

#-----------------------------------------------------------------------------------------------------------------------#
# slow print

def slowprint(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)

#-----------------------------------------------------------------------------------------------------------------------#
# Banner

def Banner():
    clear_screen_terminal()
    print(f'''{Y}                                        
 _____                            _____     
|     |___ ___ ___ ___ ___ ___   |  _  |___ 
| | | | .'|   | .'| . | -_|  _|  |   __|  _|
|_|_|_|__,|_|_|__,|_  |___|_|    |__|  |___|
                  |___| \n{B}version : 3.1.0                
{W}''')

def table():
    table = PrettyTable()
    print("\033[97;1m")
    table.field_names = [f'{B}ID{W}', f'{M}Tools{W}']
    table.add_row([f'{G}1{W}', f'{Y}Hide Windows watermark{W}'])
    table.add_row([f'{G}2{W}', f'{Y}Activate and activate windows{W}'])
    table.add_row([f'{G}3{W}', f'{Y}Show activation key for windows{W}'])
    table.add_row([f'{G}4{W}', f'{Y}chacking update & security for windows system{W}'])
    table.add_row([f'{G}5{W}', f'{Y}Network and Communications Service{W}'])
    table.add_row([f'{G}6{W}', f'{Y}Install or Uninstall WSL Microcoft windows{W}'])
    table.add_row([f'{G}7{W}', f'{Y}Install Driver Microsoft C++ and C# for Windows{W}'])
    table.add_row([f'{G}8{W}', f'{Y}Dealing with Python{W}'])
    table.add_row([f'{G}9{W}', f'{Y}Gamming play classic{W}'])
    table.add_row([f'{G}10{W}', f'{Y}Waste your time in html{W}'])
    table.add_row([f'{G}11{W}', f'{Y}zip file or folder{W}'])
    table.add_row([f'{G}12{W}', f'{Y}Tools MicroSoft Windows{W}'])
    table.add_row([f'{G}13{W}', f'{Y}osint informations{W}'])
    table.add_row([f'{G}14{W}', f'{Y}About Developr the Application{W}'])
    table.add_row([f'{G}15{W}', f'{Y}Uninstall Manager Pc{W}'])
    print(table)
    DateTime()

#-----------------------------------------------------------------------------------------------------------------------#
# main

def main():
    try:
        while True:
            choice = input(f'{R}┌─[{M}Mohammed Al-Baqer{Y}@{B}WSL.IQ{R}]─[{G}Enter number options{R}]\n└──╼ {R}>{Y}>{G}>{B} ')

            if choice == '1':
                clear_screen_terminal()
                os.system('slmgr /rearm')
                restart = input(f'{Question} Do you restart system? {Y}(y/n):{B} ')

                if restart == 'y' or restart == 'Y':
                    os.system('shutdown /r /t 0')
                    break

                elif restart == 'n' or restart == 'N':
                    sys.exit(0)
                    break

                else:
                    nothing = input(f'{Question} Sorry! is your choice Enter False please Do you Try Again? {Y}(y/n):{B} ')

                    if nothing == 'y' or nothing == 'Y':
                        continue

                    elif nothing == 'n' or nothing == 'N':
                        sys.exit()
                        break

                    else:
                        sys.exit()

            elif choice == '2':
                clear_screen_terminal()
                powershell_command = 'irm https://get.activated.win | iex'
                result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True)
                print(f"{G}Output: {Y}", result.stdout)
                print(f"{R}Error: {Y}", result.stderr)
                Back_Menu()

            elif choice == '3':
                clear_screen_terminal()
                print(f'{INFO} Key ID Name and Activation Code for Windows Key{Y}')
                os.system('wmic path SoftwareLicensingService get OA3xOriginalProductKey')
                os.system('slmgr /ato')
                Back_Menu()

            elif choice == '4':
                clear_screen_terminal()
                print(f'''{Y}
                     ___                    
                    __H__{Y}  _    _ _      
 ___ ___ ___ _ _ ___ [{Back.RED}.{S}{Y}] {Y}_| |_ | | |
|_ -| -_|  _| | |  _|[{Back.RED}.{S}{Y}]{Y}|_   _||_  |
|___|___|___|___|_|  [{Back.RED}.{S}{Y}]  {Y}|_|  |___|
                      V  
{G}By {W}: {B}Mohammed Al-Baqer    
{W}''')
                print(f'{G}[1] {Y}chack update windows system{W}')
                print(f'{G}[2] {Y}Window system cleaning and scanning{G}')
                print(f'{G}[3] {Y}generate for password{G}')
                print(f'{G}[4] {Y}Encrypt and Decrypt images audio and binary{G}')
                print(f'{G}[5] {Y}control for folder by Show and hide{G}')
                print(f'{G}[6] {Y}System Process Monitoring{G}')
                print(f'{G}[7] {Y}upgrade applications for windows system{W}')
                print(f'{G}[8] {Y}generate password GUI{W}')
                print(f'{G}[9] {Y}generate password GUI by website HTML{W}')
                print(f'{G}[10] {Y}open BIOS{G}')
                print(f'{G}[11] {Y}Fix Bug problem Windows system{W}')
                print(f'{G}[12] {Y}task manager security windows system{W}')
                print(f'{G}[13] {Y}exit{G}')

                choice_security = input(f'{Enter} Enter choice from option:{Y} ')

                if choice_security == '1':
                    chack_network_system.networking()
                    Back_Menu()
                    break
                
                elif choice_security == '2':
                    clear_screen_terminal()
                    print(f'{sign} Cleaning temporary files{G}')
                    os.system("del /q /s /f %temp%\\*")
                    print(f'{sign} Disk Cleanup is running...{G}')
                    os.system("cleanmgr /sagerun:1")
                    print(f'{sign} System files are being checked{G}')
                    os.system("sfc /scannow")
                    print(f'{sign} Hard disk is being checked.{G}')
                    os.system("chkdsk /f /r")
                    reboot = input(f'{Question} Do you Restart System? {Y}(y/n):{R} ')
                    if reboot == 'y' or reboot == 'Y':
                        os.system('shutdown /r /t 0')
                        break
                    elif reboot == 'n' or reboot == 'N':
                        Back_Menu()
                        break
                    else:
                        continue

                elif choice_security == '3':
                    clear_screen_terminal()
                    passwords()
                    Back_Menu()
                    break

                elif choice_security == '4':
                    clear_screen_terminal()
                    Encrypt_decrypt_images_audio_binary()
                    Back_Menu()
                    break

                elif choice_security == '5':
                    clear_screen_terminal()
                    folder()
                    Back_Menu()
                    break

                elif choice_security == '6':
                    clear_screen_terminal()
                    SystemWinsows.manager_task_system()
                    Back_Menu()
                    break

                elif choice_security == '7':
                    WindowsGet.winget()
                    Back_Menu()
                    break

                elif choice_security == '8':
                    app = QtWidgets.QApplication(sys.argv)
                    window = PasswordGeneratorApp()
                    window.show()
                    sys.exit(app.exec_())
                    Back_Menu()
                    break
                
                elif choice_security == '9':
                    os.system(r'html\password.html')
                    Back_Menu()
                    break
                
                elif choice_security == '10':
                    clear_screen_terminal()
                    print(f'''{B}
   ___   _____  ___  __    
  / __\  \_   \/___\/ _\   
 /__\//   / /\//  //\ \    
/ \/  \/\/ /_/ \_// _\ \   
\_____/\____/\___/  \__/   
{G}By {W}: {B}Mohammed Al-Baqer                          
{W}''')
                    bios = input(f'{Enter} Do you go to BIOS? {Y}(y,n): {M}')
                    if bios == 'y' or bios == 'Y':
                        BIOS.BIOS_Loading()
                        print(f'{R}~> {B}Shut Down system')
                        time.sleep(1)
                        os.system(r'commanding\BIOS.lnk')

                    elif bios == 'n' or bios == 'N':
                        Back_Menu()
                        break

                    else:
                        continue
                    
                elif choice_security == '11':
                    os.system(r'commanding\FixBug.cmd')
                    Back_Menu()
                    break

                elif choice_security == '12':
                    clear_screen_terminal()
                    if __name__ == "__main__":
                        TaskManager.run_hardening_tool()
                        Back_Menu()
                        break

                elif choice_security == '13':
                    Back_Menu()
                    break

            elif choice == '5':
                table = PrettyTable()
                clear_screen_terminal()
                print(f"""
      {G}\ | /{W}                                                     
     {B}-- {R}O{B} --{W}                                                    
       {G}/|\          
      {G}/\|/\             
     {G}/  |  \                 
    {G}/\/\|/\/\                  
   {G}/    |    \   
  -     -     -
 {G}By {W}: {B}Mohammed Al-Baqer{W}""")
                table.field_names = [f'{B}ID{W}', f'{M}Tools{W}']
                table.add_row([f'{G}1{W}', f'{Y}Show informations Network{W}'])
                table.add_row([f'{G}2{W}', f'{Y}Network Traffic Monitoring{W}'])
                table.add_row([f'{G}3{W}', f'{Y}Port Forwarding{W}'])
                table.add_row([f'{G}4{W}', f'{Y}show password network{W}'])
                table.add_row([f'{G}5{W}', f'{Y}Internet Speed Test Ping (ISTP){W}'])
                table.add_row([f'{G}6{W}', f'{Y}open website browser speed test{W}'])
                table.add_row([f'{G}7{W}', f'{Y}Search on proxy{W}'])
                table.add_row([f'{G}8{W}', f'{Y}exit{W}'])
                print(table)
                choice_network = input(f'{Enter} Enter choice numper for options: {Y}')

                if choice_network == '1':
                    clear_screen_terminal()
                    print(f"{INFO} system is {W}: {B}Windows{W}")
                    wifi_info = get_wifi_info()

                    for key, value in wifi_info.items():
                        print(f"{key}: {value}")
                    Back_Menu()
                    break
                
                elif choice_network == '2':
                    clear_screen_terminal()
                    monitor_traffico(1)
                    Back_Menu()
                    break
                
                elif choice_network == '3':
                    clear_screen_terminal()
                    psol()
                    Back_Menu()
                    break
                
                elif choice_network == '4':
                    clear_screen_terminal()
                    show_password_network()
                    Back_Menu()
                    break

                elif choice_network == '5':
                    clear_screen_terminal()
                    istp()
                    Back_Menu()
                    break

                elif choice_network == '6':
                    clear_screen_terminal()
                    server_st()
                    Back_Menu()
                    break

                elif choice_network == '7':
                    proxy.main()
                    Back_Menu()
                    break
                
                elif choice_network == '8':
                    break

                else:
                    print(f'{ERROR} the choice not Agree !')

                    Refresh = input(f'{Question} Do you Try Again Anyway? {Y}(y/n){W}: {Y}')

                    if Refresh == 'y' or Refresh == 'Y':
                        continue

                    elif Refresh == 'n' or Refresh == 'N':
                        break

                    else:
                        sys.exit(0)

            elif choice == '6':
                clear_screen_terminal()
                print(fr"""
            {W}•{B}_{W}•      
            {Back.YELLOW}oo{S}{B}|          
           / '\'        
          {Back.YELLOW}({S}{B}\_;/{Back.YELLOW}){S}{B}            
     _ _ _ _____ __    
    | | | |   __|  |   
    | | | |__   |  |__ 
    |_____|_____|_____|{W}
    {G}By {W}: {B}Mohammed Al-Baqer    
""")
                print(f'{G}[1] {Y}Install wsl{W}')
                print(f'{G}[2] {Y}uninstall wsl{W}')
                print(f'{G}[3] {Y}Exit{W}')

                choice_wsl = input(f'{Enter} Enter choice number: ')

                if choice_wsl == '1':
                    wsl()
                    Back_Menu()

                elif choice_wsl == '2':
                    uninstall_wsl()

                elif choice_wsl == '3':
                    print(f'{sign} Exit...{W}')
                    Back_Menu()
                    break

            elif choice == '7':
                try:
                    clear_screen_terminal()
                    print(f'''{G}
   ___   _  __    __        
  / __| (_) \ \   \ \       
 | (__   _   \ \   > >      
  \___| (_)   \_\ /_/   ___ 
                       |___|
  {G}By {W}: {B}Mohammed Al-Baqer{W}''')
                    print('\n ' + G + '{' + B + '<' + Y + '/' + B + '>' + M + '_' + G + '}' + f'\n{B} CODE\n{G} IS ASCLL ART\n' + W)
                    print(f'{G}[1] {B}installing software or setting up components on a Windows system{W}')
                    print(f'{G}[2] {B}Installing {Y}C++ {B}System Components{W}')
                    print(f'{G}[3] {B}installing {M}C# {G}.NET SDK {B}for Windows{W}')
                    print(f'{G}[4] {B}installing Microsoft Visual Studio 2022 for Windows{W}')
                    print(f'{G}[5] {B}downloading PyCharm Python IDLE for Windows{W}')
                    print(f'{G}[6] {B}Download Frameworks node.js{W}')
                    print(f'{G}[7] {Y}Exit{W}')
                    chpoce_cpp = input(f'{Enter} Enter choice options: {Y}')

                    if chpoce_cpp == '1':
                        clear_screen_terminal()
                        print(f'''
{S}          {Back.RED}     {Back.GREEN}     {S}
{S}          {Back.RED}     {Back.GREEN}     {S}
{S}          {Back.BLUE}     {Back.YELLOW}     {S}
{S}          {Back.BLUE}     {Back.YELLOW}     {S}{C}                                                                              
{W}''')
                        os.chdir('PackageMicrosoft')
                        subprocess.run(['msiexec', '/i', 'setup.msi'], check=True)
                        Back_Menu()
                        break

                    elif chpoce_cpp == '2':
                        clear_screen_terminal()
                        print(f'''{B}
_________                    
\_   ___ \    __       __    
/    \  \/ __|  |_____|  |___
\     \______    __/__    __/
 \______  /  |__|     |__|   
        \/                   
{G}By {W}: {B}Mohammed Al-Baqer{W}''')
                        os.chdir('PackageMicrosoft')
                        subprocess.run(['cmd', '/c', 'install_all.bat'], check=True)
                        Back_Menu()
                        break

                    elif chpoce_cpp == '3':
                        clear_screen_terminal()
                        print(f'''{M}
 ▄▄█▀▀▀▄█           
▄█▀     ▀    ██ ██   
██         █████████ 
▀█▄      ▄   ██ ██   
 ▀▀█▄▄▄▄▀  █████████ 
             ██ ██   
{G}By {W}: {B}Mohammed Al-Baqer{W}''')
                        webbrowser.open('https://dotnet.microsoft.com/en-us/download/dotnet/8.0')
                        Back_Menu()
                        break

                    elif chpoce_cpp == '4':
                        clear_screen_terminal()
                        print(f'''{G}
   ___   _  __    __        
  / __| (_) \ \   \ \       
 | (__   _   \ \   > >      
  \___| (_)   \_\ /_/   ___ 
                       |___|
    {G}By {W}: {B}Mohammed Al-Baqer {W}''')
                        print(f'{G}[1] {B}Microsoft Visual Studio 2022 (Community){W}')
                        print(f'{G}[2] {B}Microsoft Visual Studio 2022 (Professional){W}')
                        print(f'{G}[3] {B}Microsoft Visual Studio 2022 (Enterprise){W}')
                        print(f'{G}[4] {B}Exit{W}')

                        VS = input('Enter version Microsoft Visual Studio IDE: ')

                        if VS == '1':
                            webbrowser.open('https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false')
                            Back_Menu()
                            break

                        elif VS == '2':
                            webbrowser.open('https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false')
                            Back_Menu()
                            break

                        elif VS == '3':
                            webbrowser.open('https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Enterprise&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false')
                            Back_Menu()
                            break

                        elif VS == '4':
                            Back_Menu()
                            break

                        else:
                            sys.exit(0)

                    elif chpoce_cpp == '5':
                        clear_screen_terminal()
                        print(f'''{B}         
 _____     _____ _                 
|  _  |_ _|     | |_ ___ ___ _____ 
|   __| | |   --|   | .'|  _|     |
|__|  |_  |_____|_|_|__,|_| |_|_|_|
      |___|                        {W}\n''')
                        webbrowser.open('https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows')
                        Back_Menu()
                        break

                    elif chpoce_cpp == '6':
                        clear_screen_terminal()
                        print(f'''{Y}
  _   _           _         _     
 | \ | | ___   __| | ___   (_)___ 
 |  \| |/ _ \ / _` |/ _ \  | / __|
 | |\  | (_) | (_| |  __/_ | \__ \
 |_| \_|\___/ \__,_|\___(_)/ |___/
                         |__/     {W}\n''')
                        print(f'{G}[1] {B}Download Frameworks Node.js (.zip)')
                        print(f'{G}[2] {B}Download Frameworks Node.js (.msi)')
                        print(f'{G}[3] {B}Exit{W}')
                        node_js = input(f'{Enter} Enter choice option: ')

                        if node_js == '1':
                            webbrowser.open('https://nodejs.org/dist/v22.14.0/node-v22.14.0-win-x64.zip')
                            Back_Menu()
                            break
                        
                        elif node_js == '2':
                            webbrowser.open('https://nodejs.org/dist/v22.14.0/node-v22.14.0-x64.msi')
                            Back_Menu()
                            break
                        
                        elif node_js == '3':
                            Back_Menu()
                            break

                        else:
                            sys.exit(0)

                    elif chpoce_cpp == '7':
                        Back_Menu()
                        break

                    else:
                        continue

                except Exception:
                    pass
                    Back_Menu()
                    break

            elif choice == '8':
                table = PrettyTable()
                clear_screen_terminal()
                print(rf'''{B}
                __   /\                   
______ ____ ___/  |_|  |__   ____   ____  
\____ \\   |  |   __\  |  \ / __ \ /    \ 
|  |_\ \\___  ||  | |      \  \_\ )   |  \
|   ___// ____||__| |___|  /\____/|___|  /
|__|    \/               \/            \/                                                                                                                                                                                    
                {G}By {W}: {B}Mohammed Al-Baqer {W}{W}''')
                table.field_names = [f'{B}ID{W}', f'{M}Tools{W}', f'{Y}Whit Wowking?{W}']
                table.add_row([f'{G}1{W}', f'{Y}Python Package{W}', f'{C}Task Manager for Python and pip Package{W}'])
                table.add_row([f'{G}2{W}', f'{Y}Python Executable{W}', f'{C}transformation file from (.py) to (.exe){W}'])
                table.add_row([f'{G}3{W}', f'{Y}Refres pip{W}', f'{C}Installing and managing Python environment packages{W}'])
                table.add_row([f'{G}4{W}', f'{Y}Exit{W}', f'{C}exit from the program{W}'])
                print(table)
                choice_python = input(f'{Enter} Enter choice number from options {B}~{G}> {Y}')

                if choice_python == '1':
                    clear_screen_terminal()
                    python_package_manager()
                    Back_Menu()
                    break

                elif choice_python == '2':
                    clear_screen_terminal()
                    Python_Executable()
                    Back_Menu()
                    break

                elif choice_python == '3':
                    clear_screen_terminal()
                    get_pip.main()
                    Back_Menu()
                    break

                elif choice_python == '4':
                    Back_Menu()
                    break

                else:
                    print(f'{ERROR} the choice not Agree !')
                    Refresh = input(f'{Question} Do you Try Again Anyway? {Y}(y/n){W}: {Y}')
                    
                    if Refresh == 'y' or Refresh == 'Y':
                        continue

                    elif Refresh == 'n' or Refresh == 'N':
                        break

                    else:
                        sys.exit(0)

            elif choice == '9':
                clear_screen_terminal()
                console = Console()
                table = Table(title="Tools AI")
                table.add_column("ID", justify="right", style="cyan", no_wrap=True)
                table.add_column("Tools", style="magenta")

                table.add_row("1", "Game play XO")
                table.add_row("2", "Exit")
                console.print(table)
                
                Tools = input(f'{Enter} Enter choice number from Tolls AI: {Y}')

                if Tools == '1':
                    clear_screen_terminal()
                    XO.play_XO()
                    Back_Menu()
                    break

                elif Tools == '2':
                    Back_Menu()
                    break

                else:
                    print(f'{ERROR} the choice not Agree !')
                    Refresh = input(f'{Question} Do you Try Again Anyway? {Y}(y/n){W}: {Y}')
                    if Refresh == 'y' or Refresh == 'Y':
                        continue

                    elif Refresh == 'n' or Refresh == 'N':
                        break

                    else:
                        sys.exit(0)

            elif choice == '10':
                clear_screen_terminal()
                print(f'{G}[1] {B}drigon{W}')
                print(f'{G}[2] {B}tracking motion car{W}')
                print(f'{G}[3] {B}Exit{W}')

                choice_html = input(f"\n{Enter} Enter choice options: {Y}")

                if choice_html == '1':
                    clear_screen_terminal()
                    os.system(r'html\drigon.html')
                    Back_Menu()
                    break

                elif choice_html == '2':
                    clear_screen_terminal()
                    os.system(r'html\tracking-motion-car.html')
                    Back_Menu()
                    break

                elif choice_html == '3':
                    clear_screen_terminal()
                    Back_Menu()
                    break

                else:
                    continue

            elif choice == '11':
                clear_screen_terminal()
                zip.pyzip()
                Back_Menu()
                break

            elif choice == '12':
                clear_screen_terminal()
                console = Console()
                table = Table(title="Tools AI")
                table.add_column("ID", justify="right", style="cyan", no_wrap=True)
                table.add_column("Tools", style="magenta")
                table.add_row("1", "setup MicroSoft windows 10")
                table.add_row("2", "setup MicroSoft windows 11")
                table.add_row("3", "Exit")
                console.print(table)
                choice_MicroSoft_Windows = input(f'{Enter} Enter choice Options: {Y}') 
                try:
                    if choice_MicroSoft_Windows == '1':
                        clear_screen_terminal()
                        webbrowser.open('https://go.microsoft.com/fwlink/?LinkId=2265055')
                        Back_Menu()
                        break

                    elif choice_MicroSoft_Windows == '2':
                        clear_screen_terminal()
                        webbrowser.open('https://www.microsoft.com/en-us/software-download/windows11')
                        Back_Menu()
                        break

                    elif choice_MicroSoft_Windows == '3':
                        Back_Menu()
                        break

                    else:
                        continue

                except KeyboardInterrupt:
                    pass
            
            elif choice == '13':
                clear_screen_terminal()
                print(f"""
       {R}_,.                   
     {R},` -.)                  
    {R}( _{W}{Y}/-\{Y}-._               
   {R}/,{Y}|`--._,-^|           {Y}/|{W} 
   {R}\_{Y}| {G}|`-._/|{Y}|          {Y}/ |{W} 
     {Y}|  {G}`-, /{Y} |         {Y}/  /{W} 
     {Y}|     {G}||{Y} |        {Y}/  /{W}  
      {Y}`r-._{G}||{Y}/   {B}__   {Y}/  /{W}   
  {B}__,-<_     )`-/  `.{Y}/  /{W}    
 {B}/\   `---    \   / {Y}/  /{W}     
 {B}|   |           |.{Y}/  /{W}      
 {B}|    /          /{Y}/  /{W}       
 {B}\_/  \         |{Y}/  /{W}        
  {B}|    |   _,^- {Y}/  /{W}         
  {B}|    , ``  {Y}(\{Y}/  /_{W}          {B}.{W}
   {B}\,.->._    {Y}\X-=/^{W}         {B}/ \{W}       _            
   {B}(  /   `-._{Y}//^`{W}  ___  ___ {B}| |{W} _ __ | |_          
    {B}`Y-.____{Y}(__){W}   / {R}_{W} \/ __|{B}|.|{W}| '_ \| __|           
     {B}|     {Y}(__){B}|{W}  | {R}(0){W} \__ \{B}|.|{W}| | | | |_            
     {B}|_________|   {W}\_{R}^{W}_/|___/{B}|:|{W}|_| |_|\__|   {G}By {W}: {Y}Mohammed Al-Baqer{W}
                             {B}|:|{W}
                          {W}~{Y}\==8==/{W}~{R}
                              8
                              0{W} """)
                print(f'{G}[1] {B}informations instagram osint{W}')
                print(f'{G}[2] {B}find About phone using instagram or Dont using{W}')
                print(f'{G}[99] {B}Exit{W}')
                info_insta = input(f'{Enter} Enter choice options: {Y}')

                if info_insta == '1':
                    clear_screen_terminal()
                    Information_Instagram.Information_Instagram()
                    Back_Menu()
                    break

                elif info_insta == '2':
                    clear_screen_terminal()
                    find_phone_insta.instagram_number()
                    Back_Menu()
                    break

                elif info_insta == '99':
                    Back_Menu()
                    break

            elif choice == '14':
                notification()
                clear_screen_terminal()
                print(background("\033[97;1m" + " About Developer ", "Yellow"))
                Drowing = f'{R}~{M}>'

                slowprint(f'''{G}Hello everyone
{B}I introduce myself as 
{Drowing}{Y} Mohammed Al-Baqer
{Drowing}{Y} From Iraq 
{M}an independent software developer specializing in the famous programming language Python{B}
I developed this program specifically to manage your Windows system well
and it has most of the auxiliary tools
you need in your system from networks security and control of system management and components
For more subscribe to my Telegram channel.{W}\n''')
                version.version_App()
                
                channel_Telegram = input(f'{Question} Do you want to visit the channels me? (y/n): ')

                if channel_Telegram == 'y' or channel_Telegram == 'Y':
                    print(f'{Running} channels is being opened{W}')

                    def loading():
                        loading_symbols = [f'{R}|', f'{G}/', f'{B}-', f'{Y}\\']
                        print("Loading", end=" ", flush=True)
                        for i in range(20):
                            symbol = loading_symbols[i % len(loading_symbols)]
                            print(f'\rLoading... {symbol}', end='', flush=True)
                            time.sleep(0.09)
                    loading()

                    webbrowser.open('https://linktr.ee/wsl.iq')
                    print('\n')
                    Back_Menu()
                    break

                elif channel_Telegram == 'n' or channel_Telegram == 'N':
                    print(f'{sign} Thank you for visiting the program.{W}\n')
                    Back_Menu()
                    break

                else:
                    continue

            elif choice == '15':
                clear_screen_terminal()
                uninstall.uninstall()
                Back_Menu()
                break

            else:
                print(f'{ERROR} the choice not Agree !')
                Refresh = input(f'{Question} Do you Try Again Anyway? {Y}(y/n){W}: {Y}')

                if Refresh == 'y' or Refresh == 'Y':
                    continue

                elif Refresh == 'n' or Refresh == 'N':
                    break

                else:
                    sys.exit(0)

    except KeyboardInterrupt:
        print(f'{Running} Exit {W}')
        
if __name__ == '__main__':
    Banner()
    slowprint(f'{M}Program Development {C}[{G}Manager Pc{C}] {M}for Windows {Y}[{B}By {W}: {G}Mohammed Al-Baqer{Y}]{W}')
    table()
    main()
