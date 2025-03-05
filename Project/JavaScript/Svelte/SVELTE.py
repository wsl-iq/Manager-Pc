import os
import webbrowser

def SVELTE():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/sveltejs/svelte.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    SVELTE()