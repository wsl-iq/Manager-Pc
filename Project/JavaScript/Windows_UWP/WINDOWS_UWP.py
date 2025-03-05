import os
import webbrowser

def WINDOWS_UWP():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://learn.microsoft.com/en-us/windows/uwp/get-started/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    WINDOWS_UWP()