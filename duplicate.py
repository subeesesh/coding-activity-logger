def is_duplicate(sheet, platform, problem,data):
    records = sheet.get_all_records()
    for row in records:
        if row["Platform"] == platform and row["Problem"] == problem and row["Date"]==data:
            return True
    return False
