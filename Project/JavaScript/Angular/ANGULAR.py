import os
import webbrowser

def ANGULAR():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://angularjs.org/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    ANGULAR()