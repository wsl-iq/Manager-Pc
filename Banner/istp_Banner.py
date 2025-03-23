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

def ISTP__WIN():
    print(f"""
      {G}\ | /{W}                                                     
     {B}-- {R}O{B} --{W}                                                    
       {G}/|\       {B} ___  ____________________________{W}             
      {G}/\|/\      {B}|   |/   _____/__    ___/______   \{W}            
     {G}/  |  \     {B}|   |\_____  \  |    |   |     ___/{W}            
    {G}/\/\|/\/\    {B}|   |/        \ |    |   |    |{W}                
   {G}/    |    \   {B}|___|_______  / |____|   |____|
  -     -     -        {B}      \/{W}                            
 {Back.RED}{W} [Internet Speed Test Ping] {S}{W}""")
    
if __name__ == '__main__':
    ISTP__WIN()