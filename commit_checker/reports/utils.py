import json
import os
from colorama import Fore


def export_json(folderPath, data, fileName):
    filePath = os.path.join(folderPath, fileName)

    with open(filePath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_data(result: dict):
    n = len(result["rules"])
    d = {
        "commit": result["commit"],
        "message": result["message"],
    }
    for item, rule in result["rules"].items():
        d[item] = rule["description"]
    d["note"] = f"{result["note"]}/{n}"

    return d


def check_level_note(note, maxNote):
    percentage = (note / maxNote) * 100
    if percentage >= 90:
        return "Excellent"
    elif 90 > percentage >= 80:
        return "Very good"
    elif 80 > percentage >= 65:
        return "Good"
    elif 65 > percentage >= 50:
        return "Average"
    elif 50 > percentage >= 30:
        return "Below average"
    elif 30 > percentage >= 10:
        return "Poor"
    else:
        return "Very poor"
