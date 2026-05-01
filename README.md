# 🔐 File Integrity Monitor (GUI + Alerts + Auth)

A modern Python application to monitor file integrity using **SHA-256 hashing**, featuring a **GUI dashboard**, **secure login system**, **real-time monitoring**, and **multi-channel alerts** (desktop, email, WhatsApp).

---

## ✨ Highlights

* 🧩 **Modular architecture** (clean, maintainable code)
* 🖥️ **GUI Dashboard (Tkinter)** with live status, history & timeline
* 🔐 **Authentication system** (JSON + bcrypt hashing, multi-user)
* ⚡ **Real-time monitoring** (auto-refresh loop)
* 📂 **Folder & file scanning**
* 🔔 **Alerts**: console, sound, desktop notifications, email, WhatsApp
* 📊 **History + timeline graph** (in-app)
* 💾 **JSON storage** for hashes & users
* ✅ **“Accept / Save Changes”** (re-baseline modified files)

---

## 🧠 How It Works

1. Generates a **SHA-256 hash** for each file
2. Stores hashes in a local **JSON database**
3. Recomputes and compares hashes on demand or on a timer
4. If different → flags as **MODIFIED** and triggers alerts
5. User can **accept changes** to update the baseline hash

---

## 📁 Project Structure

```
file_integration_project/
│
├── main.py                  # CLI entry (menu + real-time loop)
├── gui_app.py               # GUI dashboard (login + monitoring)
├── integrity_checker.py     # Core logic (check, alerts)
├── file_ops.py              # JSON storage + logging
├── hash_utils.py            # SHA-256 hashing
├── auth.py                  # Signup/Login (bcrypt)
├── alerts.py                # Email / WhatsApp / Cloud hooks
│
├── users.json               # User database (auto-created)
├── hash_store.json          # Hash database (auto-created)
├── log.txt                  # Event logs (auto-created)
└── example.txt              # Sample file
```

---

## 🚀 Getting Started

### 1) Clone the repo

```
git clone https://github.com/Ahsan-Abidi/file-integrity-checker.git
cd file_integration_project
```

### 2) Install dependencies

```
pip install bcrypt plyer twilio requests
```

### 3) Run the GUI (recommended)

```
python gui_app.py
```

Or run the CLI:

```
python main.py
```

---

## 🔐 Authentication

* Multi-user system stored in `users.json`
* Passwords are **hashed using bcrypt**
* Features:

  * Signup
  * Login
  * Logout

---

## 🖥️ GUI Features

* Select file & view **status**:

  * 🟢 SAFE
  * 🔴 MODIFIED
  * 🟡 NEW
* **History panel** (timestamped events)
* **Timeline graph** (last checks)
* **Re-check** button
* **Auto-monitor** (every 5 seconds)
* **Accept / Save Changes** (update baseline hash)

---

## 🔔 Alert System

When a file is modified:

* ⚠️ Console alert
* 🔊 Sound (Windows)
* 🖥️ Desktop notification (plyer)
* 📧 Email alert (SMTP)
* 📱 WhatsApp alert (Twilio)
* ☁️ Optional cloud webhook

> ⚠️ Configure credentials in `alerts.py` before use.

---

## 📊 Logging

All events are stored in:

```
log.txt
```

Example:

```
[2026-05-01 20:10:21] MODIFIED: example.txt
```

---

## 🧪 Example Output

```
⚠️ MODIFIED: example.txt
🔔 ALERT: File has been changed!
📧 Email alert sent!
📱 WhatsApp alert sent!
```

---

## ⚠️ Limitations

* Detects changes but does not prevent them
* Desktop notifications depend on OS support
* WhatsApp requires Twilio sandbox/approval
* Not designed for enterprise-scale deployment

---

## 🔮 Future Improvements

* 📊 Advanced charts (matplotlib)
* 🗂️ Version history & rollback
* 🧾 File diff viewer (before vs after)
* 🌐 Web dashboard (Flask)
* 🔐 Role-based access (admin/user)
* ☁️ Cloud database integration

---

## 👨‍💻 Author

**Ahsan**
IT Student | Cybersecurity Learner

---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!
