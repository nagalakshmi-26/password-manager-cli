# CLI Password Manager & Generator 🔒

A simple, secure, command-line password manager and generator built with Python. Safely stores, retrieves, and generates strong random passwords protected with a master key.

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features
- **Master Key Security**: All stored credentials are encrypted/obfuscated using your personal master key.
- **Password Generator**: Creates strong, high-entropy passwords with custom length (letters, numbers, special symbols).
- **Service Lookup**: Quickly search and retrieve usernames and passwords by service name (e.g., GitHub, Gmail, Netflix).
- **Local Persistence**: Saves encrypted records in `vault.json` (zero external servers or cloud accounts required).
- **Zero External Dependencies**: Pure Python standard library (`base64`, `json`, `random`, `string`).

---

## 🚀 How to Run

### Option 1: Quick Run (Windows)
Double-click `run.bat` or run:
```cmd
run.bat
```

### Option 2: Run via Terminal
```bash
python main.py
```

---

## 📋 Sample Usage
```text
==========================================
    🔒 Simple CLI Password Manager        
==========================================
Enter your Master Vault Key: mySecretKey123

--- PASSWORD VAULT MENU ---
1. Add / Store Password
2. Retrieve a Password
3. List All Saved Services
4. Generate a Random Strong Password
5. Delete an Entry
6. Exit
```

---

## 📤 Push this project to GitHub
Open a terminal in this directory:
```bash
git init
git add .
git commit -m "Initial commit: CLI Password Manager project"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/password-manager-cli.git
git push -u origin main
```
