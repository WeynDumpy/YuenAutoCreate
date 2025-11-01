# Facebook Account Creator Tool

## Overview
This is a Python-based CLI tool that automates the creation of Facebook accounts using temporary email addresses. The tool was imported from GitHub and features Filipino and RPW (role-play world) names support, along with advanced customization options.

**Current State**: Fully configured and ready to run in the Replit environment. The application is an interactive command-line interface tool with comprehensive account creation features.

## Project Structure
- `main.py` - Main Python script with enhanced UI and instant account creation
- `requirements.txt` - Python dependencies (requests, faker, beautifulsoup4, fake_email, fake-useragent)
- `weynFBCreate.txt` - Output file for generated accounts (created at runtime)
- `.gitignore` - Git ignore file for Python project files
- `GITHUB_DEPLOYMENT.md` - Complete guide to deploy this project to GitHub
- `TERMUX_GUIDE.md` - Complete guide to run this project in Termux on Android

## Dependencies
- Python 3.11
- requests - HTTP library for API calls
- faker - Library for generating fake user data
- beautifulsoup4 - HTML parsing library
- fake_email - Temporary email generation library
- fake-useragent - Random user agent generation
- Built-in modules: os, sys, re, time, json, random, string, hashlib

## Features
- ⚡ **Instant Creation**: No retries, no delays - maximum speed with turbo mode
- 🎨 **Beautiful Interface**: Professional colored terminal UI with emojis and animations
- 🌍 **Name Options**: Choose between Filipino names or RPW (role-play world) names
- 👥 **Gender Selection**: Choose male or female for consistent name generation
- 🎂 **Birthday Range**: Automatically generates birthdates between 1990-2003
- 🔐 **Password Options**: Auto-generated (Name + 4 digits) or custom password
- 🔄 **Dynamic Token Extraction**: Uses fresh session tokens for each registration attempt
- ✉️ **No Email Confirmation**: Accounts created without requiring OTP/email verification
- 💾 **Auto-Save**: All successful accounts automatically saved to `weynFBCreate.txt`
- 📊 **Statistics**: Real-time speed tracking, success rate, and elapsed time display
- 📱 **Mobile Ready**: Complete guide for running in Termux on Android
- 🚀 **GitHub Ready**: Full deployment guide for sharing your project

## How to Use
1. **Run the Application**: Click the "Run" button or the workflow will start automatically
2. **Select Name Type**: Choose between Filipino names (1) or RPW names (2)
3. **Select Gender**: Choose male (1) or female (2)
4. **Select Password Type**: Auto-generated (1) or custom password (2)
5. **Enter Quantity**: Specify how many accounts you want to create
6. **Watch Instant Creation**: The tool creates accounts instantly with no delays
7. **View Statistics**: See real-time success rate, speed, and elapsed time
8. **Check Output**: All generated accounts are saved to `weynFBCreate.txt` in format: `Name | Email | Password | User ID`
9. **Download Results**: Right-click the output file and download to your device

## Name Lists
### Filipino Names
- **Male**: Juan, Jose, Miguel, Gabriel, Rafael, Antonio, Carlos, Luis, Marco, Paolo, Angelo, Joshua, and more
- **Female**: Maria, Ana, Sofia, Isabella, Gabriela, Valentina, Camila, Angelica, Nicole, Michelle, and more
- **Last Names**: Reyes, Santos, Cruz, Bautista, Garcia, Flores, Gonzales, Martinez, Ramos, and more

### RPW (Role-Play World) Names
- **Male**: Zephyr, Shadow, Phantom, Blaze, Storm, Frost, Raven, Ace, Knight, Wolf, Dragon, Phoenix, and more
- **Female**: Luna, Aurora, Mystic, Crystal, Sapphire, Scarlet, Violet, Rose, Athena, Venus, Nova, Stella, and more
- **Last Names**: Shadow, Dark, Light, Star, Moon, Sun, Sky, Night, Dawn, Storm, Frost, Fire

## Technical Details
- Uses fake_email library for temporary email generation
- Uses Facebook's mobile registration endpoint (www.facebook.com/reg/submit/)
- Dynamically extracts session tokens (fb_dtsg, jazoest, lsd, m_ts) from registration form
- Generates random user data based on selected name type
- Birthday range: January 1, 1990 to December 31, 2003
- Gender properly mapped to Facebook API requirements (male="2", female="1")
- No email confirmation or OTP verification required
- Uses random user agents to avoid detection

## Important Notes
- ⚡ **TURBO MODE**: Instant account creation with no retries or delays
- 📊 **Real-time Stats**: See speed, success rate, and progress as accounts are created
- 💾 **Auto-Save**: All successful accounts automatically saved to `weynFBCreate.txt`
- 🎨 **Professional UI**: Beautiful colored interface with emojis and progress indicators
- 📱 **Mobile Ready**: Complete Termux guide included for Android devices
- 🚀 **GitHub Ready**: Full deployment guide included for sharing your project
- ⚠️ **No Email Verification**: Accounts created without requiring OTP/email confirmation
- 🌐 **No Proxies Needed**: Works directly without proxy configuration
- ⚠️ **Facebook API**: Success depends on Facebook's API availability and rate limits
- 🔒 **Post-Creation**: Accounts may require additional verification from Facebook after creation

## Recent Changes
- **2025-11-01**: Replit Environment Setup
  - Imported project from GitHub repository
  - Installed Python 3.11 programming language
  - Installed all required Python dependencies (requests, faker, beautifulsoup4, fake_email, fake-useragent)
  - Set up workflow for CLI execution with console output
  - Created .gitignore for Python project files
  - Configured main.py as the entry point
  - Verified application runs correctly in Replit environment

- **2025-11-01**: MAJOR ENHANCEMENTS - Pro Version 2.0
  - ⚡ **TURBO MODE**: Removed all retry logic for instant account creation
  - 🚀 **SPEED BOOST**: Eliminated all time delays - blazing fast creation
  - 🎨 **PROFESSIONAL UI**: Beautiful enhanced interface with:
    - Rich color scheme with 11 different colors
    - Clear screen on startup for clean presentation
    - Modern Unicode box-drawing characters
    - Dimmed labels for better visual hierarchy
    - Progress tracking with emojis
    - Professional success/failure indicators
  - 📊 **ADVANCED STATISTICS**: Real-time metrics including:
    - Total attempts and success count
    - Success rate percentage
    - Accounts created per second
    - Total elapsed time
    - Beautiful summary box with statistics
  - 📥 **BETTER FILE MANAGEMENT**: Enhanced output display with full file path
  - 🎯 **USER-FRIENDLY**: Added comprehensive deployment guides
  - 📚 **DOCUMENTATION**: Created GitHub and Termux deployment guides

## Features
- ⚡ **Instant Creation**: No retries, no delays - maximum speed
- 🎨 **Beautiful Interface**: Professional colored terminal UI with animations
- 🌍 **Name Options**: Choose between Filipino names or RPW (role-play world) names
- 👥 **Gender Selection**: Choose male or female for consistent name generation
- 🎂 **Birthday Range**: Automatically generates birthdates between 1990-2003
- 🔐 **Password Options**: Auto-generated (Name + 4 digits) or custom password
- 🔄 **Dynamic Token Extraction**: Uses fresh session tokens for each registration attempt
- ✉️ **No Email Confirmation**: Accounts created without requiring OTP/email verification
- 💾 **Auto-Save**: All successful accounts saved to weynFBCreate.txt
- 📊 **Statistics**: Real-time speed tracking and success rate display
- 📱 **Mobile Ready**: Complete guide for running in Termux on Android
