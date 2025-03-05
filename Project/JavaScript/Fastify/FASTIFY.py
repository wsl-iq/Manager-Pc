import os
import webbrowser

def FASTIFY():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://github.com/fastify/fastify.git')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    FASTIFY()