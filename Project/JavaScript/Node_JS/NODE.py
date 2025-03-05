import os
import webbrowser

def NODE():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://nodejs.org/en/download/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    NODE()