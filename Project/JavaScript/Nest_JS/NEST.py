import os
import webbrowser

def NEST():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/nestjs/nest.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    NEST()