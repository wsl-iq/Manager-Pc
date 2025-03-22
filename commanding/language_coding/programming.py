import requests
from prettytable import PrettyTable

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"     # Reset
def languages_code():
    COLOR_ANSI = {
        "Python": "\033[94;1m",
        "HTML": "\033[91;1m",
        "CSS": "\033[95;1m",
        "JavaScript": "\033[93;1m",
        "PowerShell": "\033[96;1m",
        "Batchfile": "\033[90;1m",
        "Bash": "\033[92;1m",
        "C++": "\033[34;1m",
        "C#": "\033[32;1m",
        "Default": "\033[97;1m",
    }
    RESET = "\033[0m"
    BAR_LEVELS = [f"{D}▁{W}", f"{W}▂{W}", f"{R}▃{W}", f"{M}▄{W}", f"{Y}▅{W}", f"{B}▆{W}", f"{C}▇{W}", f"{G}█{W}"]
    BAR_LENGTH = 9
    username = "wsl-iq"
    repo_name = "Manager-Pc"
    API = f"https://api.github.com/repos/{username}/{repo_name}/languages"
    response = requests.get(API)

    if response.status_code == 200:
        languages = response.json()
        total_bytes = sum(languages.values())
        table = PrettyTable()
        print("\033[97;1m")
        print(f'                {W}Languages Programming Using{W}')
        table.field_names = [f"{M}ID{W}", f"{Y}Languages{W}", f"{C}Number{W}", f"{B}Usage {R}({Y}%{R}){W}", f"{G}Using{W}"]
        table.align["Languages"] = "l"
        table.align["Usage (%)"] = "r"

        for idx, (language, lines) in enumerate(languages.items(), start=1):
            percentage = (lines / total_bytes) * 100
            color = COLOR_ANSI.get(language, COLOR_ANSI["Default"])
            bar_fill = int((percentage / 100) * BAR_LENGTH)
            progress_bar = "".join([BAR_LEVELS[min(len(BAR_LEVELS)-1, i % len(BAR_LEVELS))] for i in range(bar_fill)])
            progress_bar = progress_bar.ljust(BAR_LENGTH, "▁")
            table.add_row([idx, f"{color}{language}{RESET}", f"{lines} {B}bytes{W}", f"{percentage:.2f}%", progress_bar])
        print(table)

    else:
        print(f"Error: {response.status_code}")
if __name__ == "__main__":
    languages_code()
