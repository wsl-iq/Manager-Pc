import os
import webbrowser

def VUE():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://vuejs.org/')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    VUE()