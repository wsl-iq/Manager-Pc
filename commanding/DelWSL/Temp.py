import os
def Temp():
    try:
        os.system('RemoveWSL.bat')
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    Temp()