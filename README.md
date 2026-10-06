📱 2nr Extender

A script designed to automate and extend 2nr service actions seamlessly.

> **Credits & Notice:**  
> Originally created by **sm1** on GitHub. But he left that projevt for 2-3 yrs so now I have the credits 🙂.This repository includes fixes for output handling and execution bug fixes.

---

## Quick Setup

1. Open `run.sh` in the main directory.
2. Replace the placeholder number with **6900xxxxxxx** (it's my 2nr number rn in the code)
3. Save the file and execute your script!

---

## Status Codes & Diagnostics

When running the script, pay attention to the output status code returned:

| Status Code | Indicator | Meaning | Action |
| :--- | :---: | :--- | :--- |
| `status=XXXXX`<br>*(e.g., `status=60273`)* | 🟢 **Success** | SMS sent successfully. | No further action required. |
| `status=-19`<br>`status=-21` | 🔴 **Error** | Rate-limited / anti-spam block triggered. | **Wait 4+ hours** before retrying. |

---

> **Important:** If you encounter a red error status (`-19` or `-21`), avoid repeatedly running the script right away to prevent extending your cooldown period.
