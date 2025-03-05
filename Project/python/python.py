import os
import webbrowser

def PYTHON():
    try:
        print(r'''
                __   /\                   
______ ____ ___/  |_|  |__   ____   ____  
\____ \\   |  |   __\  |  \ / __ \ /    \ 
|  |_\ \\___  ||  | |      \  \_\ )   |  \
|   ___// ____||__| |___|  /\____/|___|  /
|__|    \/               \/            \/ 
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://www.python.org/downloads/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    PYTHON()