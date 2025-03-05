import os
import webbrowser

def Professional():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Professional&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    Professional()