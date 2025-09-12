from colorama import Fore, Style

from .utils import export_json, get_data, check_level_note
from ..constants.constants import COLOR_LEVEL
import sys


def generate_report(results, output=None, format="json"):
    if results:
        if output:
            data = get_data(results)
            fileName, filePath = export_json(".", data, output, format)
            print(
                f"{Fore.GREEN}Report {fileName} exported successfully to {filePath} {Style.RESET_ALL}"
            )
            sys.exit(0)

        total_note = 0
        n = len(results[0]["rules"])
        for result in results:
            commit = result["commit"]
            levelNote = check_level_note(result["note"], n)

            print(f"{Fore.CYAN}commit: {commit}{Style.RESET_ALL}")
            print(f"message: {result['message'].strip()}")

            for item, rule in result["rules"].items():
                color = Fore.GREEN if rule["isValid"] else Fore.RED
                print(f"{item}: {color} {rule["description"]}{Style.RESET_ALL}")

            print(
                "note: "
                + f"{COLOR_LEVEL[levelNote.lower()]}{result['note']}/{n}"
                + f" ({levelNote})\n"
                + Style.RESET_ALL
            )
            total_note += result["note"]

        levelTotalNote = check_level_note(total_note, len(results) * n)
        print(
            COLOR_LEVEL[levelTotalNote.lower()]
            + "Note global: "
            + f"{total_note}/{len(results)*n}"
            + f" ({levelTotalNote})"
            + Style.RESET_ALL
        )

    else:
        print(f"{Fore.YELLOW}No commits to analyze.{Style.RESET_ALL}")
