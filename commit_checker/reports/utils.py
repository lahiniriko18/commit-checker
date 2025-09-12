import json
import os
from collections import defaultdict


def export_json(folderPath, data, fileName="report.json"):
    extension = fileName.split(".")[-1]
    if extension.lower() != "json":
        fileName += ".json"
    filePath = os.path.join(folderPath, fileName)

    with open(filePath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return fileName, filePath


def get_data(results: list):
    data = defaultdict(dict)
    total_note = 0
    n = len(results[0]["rules"])
    for result in results:
        commit = result["commit"]
        levelNote = check_level_note(result["note"], n)

        data[commit] = {
            "commit": f"Commit {result["commit"]}",
            "message": result["message"],
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
