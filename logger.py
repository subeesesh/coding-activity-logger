from datetime import datetime
from auth import sheet
from leetcode import get_recent_leetcode
from topic_classifier import classify_topic
from duplicate import is_duplicate

print("\nSelect Platform")
print("1. LeetCode")
print("2. Academy")

choice = input("Enter choice (1/2): ")

date = datetime.now().strftime("%d-%m-%Y")
time = datetime.now().strftime("%H:%M")

if choice == "1":
    USERNAME = "YOUR USERNAME"

    submissions = get_recent_leetcode(USERNAME, limit=30)

    if not submissions:
        print("❌ No recent accepted submissions found.")
        exit()

    today = datetime.now().strftime("%d-%m-%Y")
    added = 0

    for sub in submissions:
        # Convert UNIX timestamp to date
        sub_date = datetime.fromtimestamp(int(sub["timestamp"])).strftime("%d-%m-%Y")

        # 🔴 Skip if not solved today
        if sub_date != today:
            continue

        problem = sub["title"]

        # 🔴 Skip duplicates
        if is_duplicate(sheet, "LeetCode", problem):
            continue

        topic = classify_topic(problem)
        link = f"https://leetcode.com/problems/{sub['titleSlug']}"

        row = [
            today,
            "LeetCode",
            problem,
            "NA",
            topic,
            "Solved",
            link
        ]

        sheet.append_row(row)
        added += 1

    if added == 0:
        print("ℹ️ No NEW LeetCode problems solved today.")
    else:
        print(f"✅ Added {added} LeetCode problems solved today")

    exit()



elif choice == "2":
    platform = "Academy"
    added = 0

    print("\nEnter Academy problems (type 'q' to stop)\n")

    while True:
        problem = input("Problem name (q to quit): ").strip()

        if problem.lower() in ["q", "quit", "exit"]:
            break

        difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()

        topic = classify_topic(problem)

        if is_duplicate(sheet, platform, problem):
            print("⚠️ Already logged, skipping\n")
            continue

        row = [
            datetime.now().strftime("%d-%m-%Y"),
            platform,
            problem,
            difficulty,
            topic,
            "Solved",
            ""
        ]

        sheet.append_row(row)
        added += 1
        print("✅ Logged\n")

    print(f"🏁 Academy logging finished. Added {added} problems.")
    exit()


else:
    print("❌ Invalid choice")
    exit()

if is_duplicate(sheet, platform, problem):
    print("⚠️ Already logged")
    exit()

row = [date, platform, problem, difficulty, topic, "Solved", link]
sheet.append_row(row)

print("✅ Logged successfully")
