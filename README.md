# ⚡ YouTube Downloader GUI

A modern, fast, and sleek YouTube Downloader crafted with **Python** and **PyQt6**, powered under the hood by **`yt-dlp`** and **`ffmpeg`**.

Designed natively for Linux desktops with a tailored dark aesthetic, seamless anti-bot bypass mechanisms, and zero-friction media handling.

---

## ⚡ Quick Install

### Arch Linux / Manjaro

1. Install dependencies:

```bash
sudo pacman -S --needed python python-pyqt6 yt-dlp ffmpeg git
```

2. Clone repository:

```bash
git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git) ~/ytdl-gui
```

3. Enter directory:

```bash
cd ~/ytdl-gui
```

4. Run application:

```bash
python main.py
```

---

### Ubuntu / Debian / GNOME (Pop!_OS, Mint)

1. Update package lists:

```bash
sudo apt update
```

2. Install dependencies:

```bash
sudo apt install -y python3 python3-pyqt6 yt-dlp ffmpeg git
```

3. Clone repository:

```bash
git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git) ~/ytdl-gui
```

4. Enter directory:

```bash
cd ~/ytdl-gui
```

5. Run application:

```bash
python3 main.py
```

---

### Fedora (Workstation / GNOME)

1. Install dependencies:

```bash
sudo dnf install -y python3 python3-pyqt6 yt-dlp ffmpeg git
```

2. Clone repository:

```bash
git clone [https://github.com/Irmb7108/ytdl-gui.git](https://github.com/Irmb7108/ytdl-gui.git) ~/ytdl-gui
```

3. Enter directory:

```bash
cd ~/ytdl-gui
```

4. Run application:

```bash
python3 main.py
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

## 🖥️ Desktop Menu Integration

### For KDE Plasma

1. Create application entry:

```bash
mkdir -p ~/.local/share/applications
```

```bash
cat << 'EOF' > ~/.local/share/applications/ytdl-gui.desktop
[Desktop Entry]
Name=YouTube Downloader
Comment=Download YouTube Videos and
