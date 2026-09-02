```bash
cd ~/ytdl-gui

cat << 'EOF' > README.md
<div align="center">

# ⚡ YouTube Downloader GUI

A modern, fast, and sleek YouTube Downloader crafted with **Python** and **PyQt6**, powered under the hood by **`yt-dlp`** and **`ffmpeg`**.

Designed natively for Linux desktops with a tailored dark aesthetic, seamless anti-bot bypass mechanisms, and zero-friction media handling.

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=white)](https://riverbankcomputing.com/software/pyqt/)
[![yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Arch%20Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)](https://archlinux.org)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

</div>

---

## ⚡ One-Liner Quick Install (Arch Linux)

Run this single command in your terminal to install dependencies, clone the repo, set up the desktop shortcut, and launch the app immediately:

```bash
sudo pacman -S --needed --noconfirm python python-pyqt6 yt-dlp ffmpeg git && git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git) ~/ytdl-gui && cd ~/ytdl-gui && chmod +x main.py && cat << 'DESK' > ~/.local/share/applications/ytdl-gui.desktop
[Desktop Entry]
Name=YouTube Downloader
Comment=Download YouTube Videos and Audio
Exec=python /home/$USER/ytdl-gui/main.py
Icon=download-symbolic
Terminal=false
Type=Application
Categories=Network;AudioVideo;Video;Audio;
StartupNotify=true
DESK
sed -i "s/\$USER/$USER/g" ~/.local/share/applications/ytdl-gui.desktop && update-desktop-database ~/.local/share/applications 2>/dev/null && python main.py

```

---

## ✨ Features

* **🎨 Cyber Dark UI:** Polished, native-feeling dark mode with clean visual hierarchy and dynamic green neon progress tracking.
* **🎥 Flexible Video Formats:** Download in Best available resolution, 1080p, or 720p with automated audio-video multiplexing via FFmpeg.
* **🎵 Dedicated Audio Extractor:** Rip high-quality audio tracks on the fly in **MP3 (320kbps)**, **M4A / AAC**, **FLAC (Lossless)**, or **OPUS**.
* **🛡️ Built-in Anti-Bot Bypass:** Leverages mobile and multi-client spoofing (`android`, `web`, `web_safari`) to evade signature checks and bot detection flags.
* **🍪 Browser Cookie Bridge:** One-click cookie integration for Firefox, Brave, Chrome, and Chromium to effortlessly download age-restricted or private streams.
* **💾 State Persistence:** Retains custom download paths, preferred formats, and cookie configurations across restarts via `QSettings`.
* **⚡ One-Click Media Actions:** Integrated buttons to immediately play the downloaded file with your default player or open the parent directory.

---

## 📋 Supported Formats

| Mode | Format / Preset | Output Container |
| --- | --- | --- |
| **Video** | Best Available | `.mp4` |
| **Video** | 1080p Full HD | `.mp4` |
| **Video** | 720p HD | `.mp4` |
| **Audio** | MP3 (320 kbps VBR/CBR) | `.mp3` |
| **Audio** | M4A / AAC | `.m4a` |
| **Audio** | FLAC Lossless | `.flac` |
| **Audio** | OPUS | `.opus` |

---

## 🚀 Step-by-Step Manual Setup

### 1. Install Dependencies

**Arch Linux / Manjaro / EndeavourOS:**

```bash
sudo pacman -S --needed python python-pyqt6 yt-dlp ffmpeg

```

**Debian / Ubuntu:**

```bash
sudo apt update && sudo apt install -y python3 python3-pyqt6 yt-dlp ffmpeg

```

**Fedora:**

```bash
sudo dnf install -y python3 python3-pyqt6 yt-dlp ffmpeg

```

---

### 2. Clone & Run

```bash
# Clone repository
git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git)

# Enter project directory
cd ytdl-gui

# Run the application
python main.py

```

---

## 🖥️ Desktop Entry & App Launcher Integration

Add the application to your KDE Plasma / GNOME launcher menu:

```bash
mkdir -p ~/.local/share/applications

cat << 'EOF' > ~/.local/share/applications/ytdl-gui.desktop
[Desktop Entry]
Name=YouTube Downloader
Comment=Download YouTube Videos and Audio
Exec=python /home/$USER/ytdl-gui/main.py
Icon=download-symbolic
Terminal=false
Type=Application
Categories=Network;AudioVideo;Video;Audio;
StartupNotify=true
EOF

sed -i "s/\$USER/$USER/g" ~/.local/share/applications/ytdl-gui.desktop
chmod +x ~/.local/share/applications/ytdl-gui.desktop
update-desktop-database ~/.local/share/applications 2>/dev/null

```

---

## 🔄 Updating to Latest Version

To fetch updates and new features, run:

```bash
cd ~/ytdl-gui && git pull

```

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Toolkit:** PyQt6 (Qt Widgets, QProcess, QSettings)
* **Downloader Core:** [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* **Media Processor:** [FFmpeg](https://ffmpeg.org/)

---

## 👤 Author

* **ir-mb** - [GitHub Profile](https://www.google.com/search?q=https://github.com/Irmb7108)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
EOF

git add README.md
git commit -m "docs: add one-liner install commands and quick setup section"
git push

```

```
