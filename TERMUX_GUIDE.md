# 📱 Termux Guide - Run on Android

## Complete Guide to Run This Project in Termux on Android

Turn your Android phone into a powerful Facebook account creator! This guide shows you how to install and run this project in Termux.

---

## 📋 What is Termux?

Termux is a powerful Linux terminal emulator for Android that lets you run Linux commands and Python scripts on your phone - no root required!

---

## 🚀 Step 1: Install Termux

### Download Termux:

**IMPORTANT:** Don't download from Play Store (outdated version)!

**Recommended Sources:**
1. **F-Droid (Best Option):**
   - Visit: https://f-droid.org/en/packages/com.termux/
   - Download and install the APK
   - Version should be 0.118.0 or newer

2. **GitHub Releases:**
   - Visit: https://github.com/termux/termux-app/releases
   - Download: `termux-app_*.apk`

---

## ⚙️ Step 2: Initial Termux Setup

### 1. Open Termux for the First Time

When you first open Termux, it will set up automatically. Wait for it to finish.

### 2. Update Packages (IMPORTANT):

```bash
pkg update && pkg upgrade -y
```

Press **Y** (Yes) if asked to proceed.

### 3. Grant Storage Permission:

```bash
termux-setup-storage
```

This allows Termux to access your phone's storage. Click **Allow** when prompted.

---

## 🐍 Step 3: Install Python and Git

### Install Required Tools:

```bash
pkg install python git -y
```

This installs:
- Python 3.11 (the programming language)
- Git (for downloading from GitHub)
- pip (Python package manager)

### Verify Installation:

```bash
python --version
git --version
```

You should see version numbers printed.

---

## 📥 Step 4: Download the Project

### Option A: From GitHub (If you deployed it)

```bash
# Clone your repository
git clone https://github.com/your-username/facebook-account-creator.git

# Enter the directory
cd facebook-account-creator
```

### Option B: Create Manually (If you don't have GitHub)

1. **Create project folder:**
```bash
mkdir facebook-creator
cd facebook-creator
```

2. **Create main.py:**
```bash
nano main.py
```

3. **Paste your code** (copy from Replit), then:
   - Press `Ctrl + X`
   - Press `Y`
   - Press `Enter`

4. **Create requirements.txt:**
```bash
nano requirements.txt
```

5. **Add these lines:**
```
requests
faker
beautifulsoup4
fake_email
fake-useragent
```

6. Save (Ctrl+X, Y, Enter)

---

## 📦 Step 5: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Wait for all packages to install (may take 2-5 minutes).

---

## ▶️ Step 6: Run the Application

```bash
python main.py
```

🎉 **That's it!** The application should now run on your Android phone!

---

## 💡 Usage Tips for Termux

### Essential Commands:

```bash
# List files in current directory
ls

# Change directory
cd folder-name

# Go back one directory
cd ..

# Go to home directory
cd ~

# Clear screen
clear

# Exit Termux
exit
```

### File Management:

```bash
# View created accounts
cat weynFBCreate.txt

# Copy to shared storage (accessible from file manager)
cp weynFBCreate.txt ~/storage/downloads/

# The file will appear in your Downloads folder!
```

### Keyboard Shortcuts:

- **Volume Down + C** = Ctrl+C (stop program)
- **Volume Down + Z** = Ctrl+Z (suspend program)
- **Volume Down + L** = Clear screen
- **Volume Down + W** = Previous word
- **Volume Down + Q** = Previous word

---

## 🔧 Advanced Tips

### 1. Keep Session Running (Screen/Tmux)

Install tmux to keep your session running even when you close Termux:

```bash
pkg install tmux -y
```

**Usage:**
```bash
# Start tmux session
tmux

# Run your script
python main.py

# Detach session (keeps running)
Press: Ctrl+B, then D

# Reattach later
tmux attach
```

### 2. Quick Git Update (If using GitHub)

```bash
# Update code from GitHub
cd facebook-account-creator
git pull

# Install new dependencies (if any)
pip install -r requirements.txt --upgrade

# Run
python main.py
```

### 3. Create a Shortcut Script

Make running easier with a shortcut:

```bash
# Create run script
echo "cd ~/facebook-account-creator && python main.py" > ~/run-creator.sh

# Make executable
chmod +x ~/run-creator.sh

# Run from anywhere
bash ~/run-creator.sh
```

---

## 📂 File Locations in Termux

Understanding where files are stored:

```bash
# Termux home directory
/data/data/com.termux/files/home/

# Your phone's storage (after termux-setup-storage)
~/storage/

# Downloads folder
~/storage/downloads/

# Current directory
pwd
```

### Access Files from Android:

After running `termux-setup-storage`, you can access Termux files from any Android file manager:

```
Internal Storage → Android → data → com.termux → files → home
```

Or use the shared storage link at `~/storage/`

---

## 🛠️ Troubleshooting

### Problem: "pkg: command not found"
**Solution:** You're not in Termux. Make sure you're using the Termux app.

### Problem: "Permission denied"
**Solution:** Make script executable:
```bash
chmod +x main.py
```

### Problem: "Module not found"
**Solution:** Install dependencies again:
```bash
pip install -r requirements.txt --force-reinstall
```

### Problem: "Repository not found" (GitHub)
**Solution:** Check:
1. Is the repository public?
2. Is the URL correct?
3. Try HTTPS instead of SSH

### Problem: App crashes or freezes
**Solution:**
1. Close and reopen Termux
2. Clear data: Settings → Apps → Termux → Clear Data
3. Reinstall Termux from F-Droid

### Problem: Can't see created files
**Solution:** Files are in the current directory:
```bash
ls
cat weynFBCreate.txt
```

To copy to Downloads:
```bash
cp weynFBCreate.txt ~/storage/downloads/
```

---

## 🎯 Quick Reference

### Complete Workflow (After Initial Setup):

```bash
# Open Termux
cd facebook-account-creator
python main.py

# View results
cat weynFBCreate.txt

# Copy to Downloads
cp weynFBCreate.txt ~/storage/downloads/
```

---

## 🌟 Pro Tips

1. **Use a Bluetooth Keyboard:** Makes typing much easier!

2. **Install a Better Text Editor:**
```bash
pkg install vim -y
# or
pkg install nano -y
```

3. **Install Tree (visualize folders):**
```bash
pkg install tree -y
tree
```

4. **Monitor Resources:**
```bash
pkg install htop -y
htop
```

5. **Access From Computer:**
Install SSH server to access Termux from your PC:
```bash
pkg install openssh -y
sshd
```

---

## ⚠️ Important Notes

- **Battery:** Keep your phone plugged in for long sessions
- **Internet:** Ensure stable internet connection
- **Storage:** Free up at least 500MB of space
- **Permissions:** Grant storage permission when asked
- **Updates:** Keep Termux and packages updated

---

## 📱 Recommended Apps

Enhance your Termux experience:

1. **Termux:API** - Access phone features from Termux
2. **Termux:Widget** - Create home screen shortcuts
3. **Termux:Styling** - Customize colors and fonts
4. **Hacker's Keyboard** - Better keyboard for terminal

All available on F-Droid!

---

## 🆘 Getting Help

If you encounter issues:

1. **Check Termux Wiki:** https://wiki.termux.com/
2. **Termux GitHub:** https://github.com/termux/termux-app
3. **Community:** Reddit r/termux

---

## 🎉 You're All Set!

You can now run the Facebook Account Creator directly on your Android phone using Termux! No computer needed!

### What You Can Do:

✅ Create Facebook accounts on-the-go
✅ Access your projects anywhere
✅ Learn Python on your phone
✅ Run any Python script
✅ Become a mobile hacker! 😎

---

**Made with ❤️ for Android Users**

**By: WEYN DUMP**
