from colorama import Back

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

def SECURITY__WIN():
    print(f'''{Y}
                     ___                    
                    __H__{Y}  _    _ _      
 ___ ___ ___ _ _ ___ [{Back.RED}.{S}{Y}] {Y}_| |_ | | |
|_ -| -_|  _| | |  _|[{Back.RED}.{S}{Y}]{Y}|_   _||_  |
|___|___|___|___|_|  [{Back.RED}.{S}{Y}]  {Y}|_|  |___|
                      V  
{W}''')
    
if __name__ == '__main__':
    SECURITY__WIN()