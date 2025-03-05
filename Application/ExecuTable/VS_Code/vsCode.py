import os
import webbrowser

def vscode():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    vscode()