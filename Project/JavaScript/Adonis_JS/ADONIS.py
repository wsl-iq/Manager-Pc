import os
import webbrowser

def ADONIS():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/adonisjs/core.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    ADONIS()