import os
import webbrowser

def EXPRESS():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/expressjs/express.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    EXPRESS()