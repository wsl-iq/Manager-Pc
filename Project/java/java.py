import os
import webbrowser

def JAVA():
    try:
        print('''
     /\                     
    |  |____  ___  ______   
    |  |__  \ \  \/ /__  \  
/\__|  |/ __ \_\   / / __ \_
\_____/(____  / \_/ (____  /
            \/           \/ 
''')
        os.system('cls' if os.name == 'nt' else 'clear')
        webbrowser.open('https://javadl.oracle.com/webapps/download/AutoDL?BundleId=251639_7ed26d28139143f38c58992680c214a5')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    JAVA()