import os
import webbrowser

def PyCharm():
    try:
        print('''
 _____     _____ _                 
|  _  |_ _|     | |_ ___ ___ _____ 
|   __| | |   --|   | .'|  _|     |
|__|  |_  |_____|_|_|__,|_| |_|_|_|
      |___|                        ''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    PyCharm()