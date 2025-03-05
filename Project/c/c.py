import os
import webbrowser

def C():
    try:
        print('''
_________  
\_   ___ \ 
/    \  \/ 
\     \____
 \______  /
        \/ 
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/Welding-Torch/installc/releases/latest/download/installc.exe')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    C()