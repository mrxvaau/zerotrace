
# ZeroTrace

> **The Easiest, Most Beautiful Criminal Tracker & Phishing Framework. Built for education, research, and red teamers.**

---

## ⚠️ FOR AUTHORIZED, ETHICAL USE ONLY!

ZeroTrace is a powerful educational and penetration testing tool.  
**Do not use this on targets you do not own or have explicit, written permission to test!**  
Authors and contributors are not responsible for misuse or illegal activity.

---

## 🚀 Features

- **Instant Phishing Site Cloning** – Clone login pages from Facebook, Instagram, Google, PayPal, and more, or supply your own custom URL.
- **One-Line Phishing Link Creation** – Integrates seamlessly with [ngrok](https://ngrok.com/) for easy web exposure.
- **Beautiful Terminal UI** – Leverages Rich for vibrant, organized victim data and credentials.
- **Real-Time Visitor Tracking** – Captures IP, device, browser, battery, GPU, language, time, and full geolocation (with Google Maps links).
- **GPS Popup** – Triggers GPS prompt on page load for maximum location accuracy.
- **Credential Logging** – Logs all form data and victim details to local JSON files.
- **Ready-to-Share Social Engineering Messages** – Sample alert/claim/verification messages provided.
- **Silent, Minimal Flask Web Server** – Runs on all major platforms.

---

## 🖼️ Screenshots

| Setup | Victim Detected | Credentials Captured |
|-------|----------------|---------------------|
| ![setup](https://user-images.githubusercontent.com/your-setup-img.png) | ![victim](https://user-images.githubusercontent.com/your-victim-img.png) | ![creds](https://user-images.githubusercontent.com/your-creds-img.png) |

*Screenshots coming soon!*

---

## ⚙️ Installation

### 1. **Clone the repo**
```bash
git clone https://github.com/mrxvaau/zerotrace.git
cd zerotrace
```

### 2. **Install Python dependencies**
> Python 3.7+ required.
```bash
pip install -r requirements.txt
```
If you get errors about `rich`, it will auto-install on first run.

### 3. **Install ngrok**  
Download from [ngrok.com](https://ngrok.com/download).

---

## 🚦 Usage

### 1. **Start ngrok in a separate terminal:**
```bash
ngrok http 5000
```

### 2. **Run ZeroTrace:**
```bash
python zerotrace.py
```

- Follow the interactive setup:  
  - Paste your ngrok URL
  - Pick a target site to clone (or custom URL)
  - Copy/share the generated phishing link

### 3. **Monitor for Victims**
- All access logs saved to `victim_logs.json`
- Credentials saved to `credentials.json`
- Real-time notifications in the terminal

---

## ⚠️ Legal Notice

ZeroTrace is **strictly for ethical hacking, red teaming, and security research**.  
**Never target systems you do not own or have written authorization to test.**  
You are solely responsible for compliance with all laws and regulations.

---

## 🛠️ Customization

- **Add new templates:**  
  Edit the `FAMOUS_SITES` dictionary in `zerotrace.py` to add/remove targets.
- **Modify tracking script:**  
  Edit the `TRACK_SCRIPT` variable for custom JS payloads.
- **Change UI and logging:**  
  All Rich-based output is in `zerotrace.py` — style away!

---

## 📦 Credits

- **Author:** [mrxvaau](https://github.com/mrxvaau)
- **Rich UI:** [Textualize Rich](https://github.com/Textualize/rich)
- **Flask:** [Flask Web Framework](https://flask.palletsprojects.com/)
- **BeautifulSoup:** [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

---

## 🌐 Disclaimer

This tool is provided for **educational purposes** only.  
Use responsibly, and always within legal and ethical boundaries.

---

**Star the repo if you like it, and open issues or PRs to contribute!**
