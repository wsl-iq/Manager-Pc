from commanding.design.colors import(R, G, B, Y, C, M, W, D, S)
from commanding.design.Terminal import(sign, Enter, ERROR, INFO, Information, Working, NotWorking, warning,
                            Complete, successfully, Failed, please, Question, Help, note, other, 
                            Running, Retrying, Ready, Loading, OK, Okay, stop, Critical, paused,
                            Retrying, Skip, SCAN, Chacking, Hacking, security, AI)
from commanding.design.BackGround import(Red, Green, Blue, Yellow, Cyan, Magenta, White, Black, Dark, Reset)
import os
import sys
import shutil 

def uninstall():
    try:
        while True:
            print(f' {G}[1] {B}Uninstall Manager PC{W}\n',f'{G}[2] {B}Exit{W}\n')
            
            uninstall_choice = input(f'{Enter} Enter your choice: {Y}')

            if uninstall_choice == '1':
                items_to_remove = [
                    'command',
                    'icon',
                    'PackageMicrosoft',
                    'server',
                    'html',
                    'About.txt',
                    'desktop.ini',
                    'setup.bat',
                    'run.exe'
                ]

                for item in items_to_remove:
                    if os.path.exists(item):
                        if os.path.isfile(item):
                            os.remove(item)
                            print(f'{INFO} File removed: {item}')
                        elif os.path.isdir(item):
                            shutil.rmtree(item)
                            print(f'{INFO} Folder removed: {item}')
                    else:
                        print(f'{please} Not found: {item}{W}')
                
                with open("cleanup.bat", "w") as batch_file:
                    batch_file.write(f"@echo off\n")
                    batch_file.write(f"timeout /t 2 >nul\n")
                    batch_file.write(f"del \"{__file__}\"\n")
                    batch_file.write(f"del cleanup.bat\n")
                
                print(f"{Running} Uninstallation complete Closing...{W}")
                
                os.system("start cleanup.bat")
                sys.exit()

            elif uninstall_choice == '2':
                print(f"{Running} Exiting...{W}")
                sys.exit()

            else:
                print(f"{ERROR} choice Please try again !{W}")
    except KeyboardInterrupt:
        print(f"\n{sign} Process interrupted by user.{W}")
        sys.exit()

if __name__ == '__main__':
    uninstall()
