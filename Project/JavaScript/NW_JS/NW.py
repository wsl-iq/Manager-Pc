import os
import webbrowser

def NW():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://nwjs.io/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    NW()