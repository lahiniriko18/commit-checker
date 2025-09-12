import json
import os
from collections import defaultdict
from colorama import Fore, Style
from ..validations.validation_reports import validate_format


def export_json(folderPath, data, fileName="report.json", format="json"):
    fileName, extension = validate_format(fileName, format)
    filePath = os.path.join(folderPath, fileName)
    if extension == "json":
        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        with open(filePath, "w", encoding="utf-8") as f:
            f.write("Commit Validation Report\n\n\n")
            for key, rule in data.items():
                if key != "total_note":
                    for item, value in rule.items():
                        f.write(
                            f"{item.capitalize()}: {value}{"\n" if item != 'message' else ''}"
                        )
                    f.write("\n")
            f.write(f"Total Note: {data['total_note']}\n")
    return fileName, filePath


def get_data(results: list):
    data = defaultdict(dict)
    total_note = 0
    n = len(results[0]["rules"])
    for result in results:
        commit = f"Commit {result["commit"]}"
        levelNote = check_level_note(result["note"], n)

        data[commit] = {
            "commit": result["commit"],
            "message": result["message"],
            "date": result["date"],
        }
        for item, rule in result["rules"].items():
            data[commit][item] = rule["description"]
        data[commit]["note"] = f"{result["note"]}/{n} ({levelNote})"
        total_note += result["note"]
    data = dict(data)
    data["total_note"] = (
        f"{total_note}/{len(results)*n} ({check_level_note(total_note, len(results)*n)})"
    )
    return data


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
