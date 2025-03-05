import os
import webbrowser

def CPP():
    try:
        print('''
_________                    
\_   ___ \    __       __    
/    \  \/ __|  |_____|  |___
\     \______    __/__    __/
 \______  /  |__|     |__|   
        \/                   
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://sourceforge.net/projects/orwelldevcpp/files/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    CPP()