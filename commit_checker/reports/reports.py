import json
import os

from colorama import Fore, Style
from collections import defaultdict


def export_json(folderPath, data, fileName):
    filePath = os.path.join(folderPath, fileName)

    with open(filePath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def generate_report(results, output=None):
    total_note = 0
    data = defaultdict(dict)
    for result in results:
        commit = result["commit"]
        print(f"{Fore.CYAN}Commit: {commit}{Style.RESET_ALL}")
        print(f"Message: {result['message'].strip()}")
        print(f"Note: {result['note']}/3")

        data[commit] = {
            "commit": commit,
            "message": result["message"],
            "note": f"{result["note"]}/3",
        }
        for item, rule in result["rules"].items():
            color = Fore.GREEN if rule["isValid"] else Fore.RED
            print(f"{item}: {color} {rule["description"]}{Style.RESET_ALL}")
            data[commit][item] = rule["description"]

        total_note += result["note"]
    print(
        f"{Fore.YELLOW} \nNote global: {total_note}/{len(results)*3} {Style.RESET_ALL}"
    )

    data = dict(data)
    data["total_note"] = f"{total_note}/{len(results)*3}"

    if output:
        export_json(output, data, "rapport.json")
