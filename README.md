# ⚡ YouTube Downloader GUI

A modern, fast, and sleek YouTube Downloader crafted with **Python** and **PyQt6**, powered under the hood by **`yt-dlp`** and **`ffmpeg`**.

Designed natively for Linux desktops with a tailored dark aesthetic, seamless anti-bot bypass mechanisms, and zero-friction media handling.

---

## ⚡ 1. Install Dependencies

Run the single-line command matching your Linux distribution:

### Arch Linux / Manjaro

```bash
sudo pacman -S --needed python python-pyqt6 yt-dlp ffmpeg git
```

### Ubuntu / Debian / Pop!_OS / Linux Mint

```bash
sudo apt update && sudo apt install -y python3 python3-pyqt6 yt-dlp ffmpeg git
```

### Fedora (Workstation / GNOME)

```bash
sudo dnf install -y python3 python3-pyqt6 yt-dlp ffmpeg git
```

---

## 🚀 2. Clone & Run

Run these commands to clone the repository and launch the app:

### Clone Repository

```bash
git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git) ~/ytdl-gui
```

### Run Application

```bash
python3 ~/ytdl-gui/main.py
```

---

## ✨ Features

- **Cyber Dark UI:** Polished, native-feeling dark mode with clean visual hierarchy.
- **Dynamic Progress Bar:** Smooth green progress tracking without percentage jumps.
- **Multiple Video Formats:** Supports Best Quality, 1080p, and 720p with auto-muxing to MP4.
- **Dedicated Audio Extractor:** Download high-bitrate MP3 (320kbps), M4A, FLAC (Lossless), or OPUS.
- **Anti-Bot Bypass:** Embedded player spoofing (Android/Web clients) to avoid YouTube bot blocks.
- **Browser Cookies Bridge:** One-click cookie import (Firefox, Brave, Chrome, Chromium).
- **Persistent Settings:** Saves your custom download path, preferred format, and cookie state.
- **Direct Playback:** Integrated buttons to play the downloaded file or open the folder immediately.

---

## 📋 Supported Formats

| Mode | Format / Preset | Output Container |
| :--- | :--- | :--- |
| Video | Best Available | .mp4 |
| Video | 1080p Full HD | .mp4 |
| Video | 720p HD | .mp4 |
| Audio | MP3 (320 kbps) | .mp3 |
| Audio | M4A / AAC | .m4a |
| Audio | FLAC Lossless | .flac |
| Audio | OPUS | .opus |

---

## 🖥️ Desktop Menu Integration (Optional)

Add the application to your system app launcher with a single command:

### For KDE Plasma

```bash
mkdir -p ~/.local/share/applications && printf "[Desktop Entry]\nName=YouTube Downloader\nComment=Download YouTube Videos and Audio\nExec=python3 %s/ytdl-gui/main.py\nIcon=download-symbolic\nTerminal=false\nType=Application\nCategories=Network;AudioVideo;Video;Audio;\nStartupNotify=true\n" "$HOME" > ~/.local/share/applications/ytdl-gui.desktop && chmod +x ~/.local/share/applications/ytdl-gui.desktop && kbuildsycoca6 2>/dev/null || kbuildsycoca5 2>/dev/null && update-desktop-database ~/.local/share/applications 2>/dev/null
```

### For GNOME

```bash
mkdir -p ~/.local/share/applications && printf "[Desktop Entry]\nName=YouTube Downloader\nComment=Download YouTube Videos and Audio\nExec=python3 %s/ytdl-gui/main.py\nIcon=folder-download-symbolic\nTerminal=false\nType=Application\nCategories=Network;AudioVideo;Video;Audio;\nStartupNotify=true\n" "$HOME" > ~/.local/share/applications/ytdl-gui.desktop && chmod +x ~/.local/share/applications/ytdl-gui.desktop && update-desktop-database ~/.local/share/applications 2>/dev/null
```

---

## 🔄 Update

To update your local installation to the latest version:

```bash
cd ~/ytdl-gui && git pull
```

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI Toolkit:** PyQt6
- **Downloader Core:** yt-dlp
- **Media Processor:** FFmpeg

---

## 👤 Author

- **ir-mb** - https://github.com/Irmb7108

---

## 📄 License

This project is licensed under the MIT License.
