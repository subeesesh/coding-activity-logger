# 🚀 Coding Activity Logger

A **production-style Python automation tool** that tracks your **daily coding activity** across multiple platforms and stores it in **Google Sheets (Excel-exportable)**.

Built to eliminate manual logging and enforce **daily consistency**.

---

## ✨ Features

* 🔄 **Automatic LeetCode logging**

  * Fetches authenticated submissions
  * Logs **only problems solved today**
* 🧠 **Auto topic classification**
* 🚫 **Duplicate prevention**
* 🔁 **Loop-based Academy logging**
* 📅 Automatic **date & time tracking**
* 📊 Google Sheets → **Excel compatible**
* 🖥️ Clean **CLI-based UX**

---

## 🏗️ Architecture

```
User solves problem
        ↓
Python CLI (logger.py)
        ↓
LeetCode GraphQL / Manual Input
        ↓
Duplicate & Date Filter
        ↓
Topic Classification
        ↓
Google Sheets (API)
        ↓
Excel Export (.xlsx)
```

---

## 📁 Project Structure

```
coding-activity-logger/
│
├── auth.py                # Google Sheets authentication
├── logger.py              # Main CLI entry point
├── leetcode.py            # LeetCode submission fetcher
├── topic_classifier.py    # Auto topic detection
├── duplicate.py           # Duplicate prevention logic
├── README.md
├── .gitignore
└── credentials.json ❌ (ignored)
```

---

## 🔐 Setup & Configuration

### 1️⃣ Google Sheets API Setup

This project uses **Google Sheets API** to store logs.

#### Steps:

1. Go to **Google Cloud Console**
2. Create a new project
3. Enable:

   * **Google Sheets API**
   * **Google Drive API**
4. Create a **Service Account**
5. Generate a **JSON key**
6. Rename it to:

   ```
   credentials.json
   ```
7. Place it in the project root
8. Share your Google Sheet with the service account email (**Editor access**)

⚠️ `credentials.json` is ignored using `.gitignore`.

---

### 2️⃣ LeetCode Session Setup (Required for Automation)

LeetCode does not provide a stable public API,
so this project uses your **authenticated session cookie**.

#### Steps:

1. Log in to **LeetCode**
2. Open **Developer Tools** (`F12`)
3. Navigate to:

   ```
   Application → Cookies → https://leetcode.com
   ```
4. Copy:

   ```
   LEETCODE_SESSION
   ```

---

### 3️⃣ Environment Variable Setup (Recommended)

Create a file:

```
.env
```

Add:

```
LEETCODE_SESSION=your_cookie_here
```

Load it in `leetcode.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
```

⚠️ `.env` is excluded from Git.

---

## 📦 Installation

```bash
pip install gspread oauth2client requests python-dotenv
```

---

## ▶️ Usage

```bash
python logger.py
```

### Options:

| Option | Description                                      |
| ------ | ------------------------------------------------ |
| 1      | Automatically logs **today’s LeetCode problems** |
| 2      | Loop-based manual logging for Academy platforms  |

---

## 📊 Output Format (Google Sheet)

| Date | Time | Platform | Problem | Difficulty | Topic | Status | Link |
| ---- | ---- | -------- | ------- | ---------- | ----- | ------ | ---- |

Export anytime as **Excel (.xlsx)**.

---

## 🔒 Security & Best Practices

* ❌ API keys and cookies are never committed
* ✅ `.gitignore` blocks sensitive files
* ✅ Session cookies stored in environment variables
* 🔐 Safe for public GitHub repositories

---

## 🧠 Design Decisions

* **Daily-only logging** avoids historical spam
* **Duplicate detection** ensures idempotency
* **Topic inference** avoids manual tagging
* **CLI-first design** keeps tool lightweight

---

## 🚀 Future Enhancements

* Difficulty & tag auto-fetch
* Charts & analytics dashboard
* Desktop / EXE packaging
* CodeChef & Codeforces integration
* Background scheduler

---

## 📌 Resume-Ready Description

> *Built a Python-based automation tool that logs daily coding activity across multiple platforms using Google Sheets API and authenticated LeetCode GraphQL requests, featuring duplicate prevention, topic classification, and Excel export support.*

---

## 🤝 Contributing

PRs and suggestions are welcome.
This project is actively evolving.

---

## ⭐ If this helped you

Give the repo a ⭐ — it motivates further improvements!

---

