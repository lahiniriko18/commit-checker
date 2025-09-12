def check_note(note, max_note):
    percentage = (note / max_note) * 100
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
