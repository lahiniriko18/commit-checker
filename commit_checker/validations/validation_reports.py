from colorama import Fore, Style
import sys


def validate_format(fileName, format):
    if format not in ["json", "txt"]:
        print(
            f"{Fore.RED}Format not supported, using json or txt format{Style.RESET_ALL}"
        )
        sys.exit(1)
    listFileName = fileName.split(".")
    extension = listFileName[-1]
    if extension in ["json", "txt"]:
        listFileName[-1] = format
    else:
        listFileName.append(format)

    fileName, extension = ".".join(listFileName), listFileName[-1]
    return fileName, extension
