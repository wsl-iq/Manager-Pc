import os
import webbrowser

def Framework():
    try:
        print(r'''
  ________________   ____  /\                       __   
 /   _____/______ \ |    |/  \        ____   ____ _/  |_ 
 \_____  \ |    |  \|       /  ______/    \_/ __ \\   __\
 /        \|    |   \    |  \ /_____/   |  \  ___/_|  |  
/_______  /_______  /____|__ \      |___|  /\___  /|__|  
        \/        \/        \/           \/     \/       
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-8.0.406-windows-x64-installer')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    Framework()