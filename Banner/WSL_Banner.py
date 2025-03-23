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

def WSL__WIN():
    print(fr"""
            {W}•{B}_{W}•      
            {Back.YELLOW}oo{S}{B}|          
           / '\'        
          {Back.YELLOW}({S}{B}\_;/{Back.YELLOW}){S}{B}            
     _ _ _ _____ __    
    | | | |   __|  |   
    | | | |__   |  |__ 
    |_____|_____|_____|{W}""")

if __name__ == '__main__':
    WSL__WIN()