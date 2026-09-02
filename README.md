# ⚡ YouTube Downloader GUI

A modern, fast, and sleek YouTube Downloader crafted with **Python** and **PyQt6**, powered under the hood by **`yt-dlp`** and **`ffmpeg`**.

Designed natively for Linux desktops with a tailored dark aesthetic, seamless anti-bot bypass mechanisms, and zero-friction media handling.

---

## ⚡ Quick Install (Arch Linux)

Run these commands in your terminal to install dependencies and run the app:

### 1. Install Dependencies
```bash
sudo pacman -S --needed python python-pyqt6 yt-dlp ffmpeg git
```

### 2. Clone & Run
```bash
git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git) ~/ytdl-gui
cd ~/ytdl-gui
python main.py
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

## 🖥️ Add to Desktop Menu (KDE / GNOME)

To launch the app directly from your application launcher, run:

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

## 🔄 Update

To update your local copy to the latest commit:

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

- **ir-mb** - [GitHub Profile](https://github.com/Irmb7108)

---

## 📄 License

This project is licensed under the MIT License.
