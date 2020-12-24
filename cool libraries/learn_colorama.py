import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
# print("\033[31;1;4mHello\033[0m")
print(Fore.RED+ "some red text")
# to stop color from continuing manually.
# print('\033[39m')
print("hello")
print(Back.WHITE + 'white')

print(Fore.RED + Back.GREEN + "red text on green background")
print(f"{Fore.CYAN}{Back.WHITE}{Style.DIM}   Cyan Text - White Background - Dim")
