import os
import webbrowser

def WINUI3():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://learn.microsoft.com/en-us/windows/apps/winui/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    WINUI3()