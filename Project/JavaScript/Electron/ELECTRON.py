import os
import webbrowser

def ELECTRON():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/electron/forge.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    ELECTRON()