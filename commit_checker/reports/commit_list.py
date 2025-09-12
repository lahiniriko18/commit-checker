from colorama import Fore, Style
from ..constants.constants import DICT_COMMIT

def list_commit():
    for item, value in DICT_COMMIT.items():
        print(f"{Fore.CYAN}{item}:" + Style.RESET_ALL + f" {value}")
