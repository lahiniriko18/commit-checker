from colorama import Fore, Style
from ..constants.constants import DICT_COMMIT

def list_commit():
    print(f"{Fore.CYAN}LIST OF COMMIT TYPE STANDARDS:{Style.RESET_ALL}")
    for item, value in DICT_COMMIT.items():
        print(f"{Fore.CYAN}{item}:" + Style.RESET_ALL + f" {value}")