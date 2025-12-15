def is_duplicate(sheet, platform, problem):
    records = sheet.get_all_records()
    for row in records:
        if row["Platform"] == platform and row["Problem"] == problem:
            return True
    return False
