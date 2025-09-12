from collections import defaultdict

from colorama import Fore, Style

from .utils import export_json, get_data, check_level_note
from ..constants.constants import COLOR_LEVEL


def generate_report(results, output=None):
    if results:
        total_note = 0
        data = defaultdict(dict)
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

            data[commit] = get_data(result)
            total_note += result["note"]

        levelTotalNote = check_level_note(total_note, len(results) * n)
        print(
            COLOR_LEVEL[levelTotalNote.lower()]
            + "Note global: "
            + f"{total_note}/{len(results)*n}"
            + f" ({levelTotalNote})"
            + Style.RESET_ALL
        )

        data = dict(data)
        data["total_note"] = f"{total_note}/{len(results)*3}"

        if output:
            export_json(output, data, "rapport.json")
    else:
        print(f"{Fore.YELLOW}No commits to analyze.{Style.RESET_ALL}")
