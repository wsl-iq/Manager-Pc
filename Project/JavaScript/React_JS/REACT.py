import os
import webbrowser

def REACT():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/facebook/react.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    REACT()