import os
import webbrowser

def PHP():
    try:
        print(r'''
        /\            
______ |  |__ ______  
\____ \|  |  \\____ \ 
|  |_\ \      \  |_\ \
|   ___/___|  /   ___/
|__|        \/|__|    
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://windows.php.net/downloads/releases/php-8.4.4-src.zip')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    PHP()