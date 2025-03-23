R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset

def network():
    print(f"""
                   {G}\ | /{W}                                                     
                  {B}-- {R}O{B} --{W}                                                    
                    {G}/|\                    
                   {G}/\|/\                 
                  {G}/  |  \                 
                 {G}/\/\|/\/\                    
                {G}/    |    \ 
               -     -     -{W}""")
if __name__ == '__main__':
    network()