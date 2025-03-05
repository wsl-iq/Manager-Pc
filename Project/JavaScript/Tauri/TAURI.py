import os
import webbrowser

def TAURI():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/tauri-apps/tauri.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    TAURI()