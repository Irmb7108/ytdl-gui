import os
import sys
import re
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLineEdit, QPushButton, QComboBox, QTextEdit, QLabel, 
    QFileDialog, QCheckBox, QProgressBar
)
from PyQt6.QtCore import QProcess, QSettings, QUrl, Qt
from PyQt6.QtGui import QDesktopServices

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("ir_mb", "YouTubeDownloader")
        
        default_dir = os.path.expanduser("~/Downloads")
        self.save_directory = self.settings.value("save_path", default_dir)
        self.saved_use_cookies = self.settings.value("use_cookies", "false") == "true"
        self.saved_browser = self.settings.value("selected_browser", "firefox")
        self.saved_quality = self.settings.value("selected_quality", "Best Video + Audio (MP4)")

        self.last_downloaded_file = None
        self.process = None
        self.download_stage = 0
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("YouTube Downloader - by ir-mb")
        self.resize(600, 650)
        self.setStyleSheet("""
            QWidget {
                background-color: #12141a;
                color: #e6edf3;
                font-family: 'Segoe UI', 'Ubuntu', sans-serif;
                font-size: 13px;
            }
            QLabel {
                font-weight: bold;
                color: #8b949e;
                margin-top: 4px;
            }
            QLabel#creator_badge {
                color: #58a6ff;
                font-family: 'JetBrains Mono', 'Fira Code', monospace;
                font-size: 11px;
                font-weight: 600;
                letter-spacing: 1px;
            }
            QLineEdit, QComboBox {
                background-color: #1c2128;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 10px;
                color: #ffffff;
                selection-background-color: #238636;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #2ea043;
            }
            QPushButton {
                background-color: #21262d;
                border: 1px solid #30363d;
                border-radius: 8px;
                padding: 10px 16px;
                font-weight: bold;
                color: #c9d1d9;
            }
            QPushButton:hover {
                background-color: #30363d;
                border-color: #8b949e;
            }
            QPushButton#download_btn {
                background-color: #238636;
                color: #ffffff;
                border: none;
                font-size: 14px;
                padding: 12px;
            }
            QPushButton#download_btn:hover {
                background-color: #2ea043;
            }
            QPushButton#download_btn:disabled {
                background-color: #1a472a;
                color: #6e7681;
            }
            QPushButton#play_btn {
                background-color: #1f6feb;
                color: #ffffff;
                border: none;
            }
            QPushButton#play_btn:hover {
                background-color: #388bfd;
            }
            QPushButton#play_btn:disabled {
                background-color: #1b2f4a;
                color: #6e7681;
            }
            QProgressBar {
                border: 1px solid #30363d;
                border-radius: 8px;
                background-color: #161b22;
                text-align: center;
                color: #ffffff;
                font-weight: bold;
                height: 22px;
            }
            QProgressBar::chunk {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #238636, stop:1 #3fb950);
                border-radius: 7px;
            }
            QTextEdit {
                background-color: #0d1117;
                border: 1px solid #30363d;
                border-radius: 8px;
                color: #7ee787;
                font-family: 'JetBrains Mono', 'Fira Code', monospace;
                font-size: 11px;
                padding: 8px;
            }
            QCheckBox {
                color: #8b949e;
            }
            QCheckBox::indicator:checked {
                background-color: #238636;
                border-radius: 3px;
            }
        """)

        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 16, 20, 16)

        # Header Title & Creator Tag
        header_layout = QHBoxLayout()
        title_label = QLabel("⚡ YouTube Downloader")
        title_label.setStyleSheet("font-size: 15px; font-weight: bold; color: #ffffff;")
        
        creator_tag = QLabel("Developed by ir-mb")
        creator_tag.setObjectName("creator_badge")
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        header_layout.addWidget(creator_tag)
        layout.addLayout(header_layout)

        # URL Input
        self.url_label = QLabel("YouTube Video URL")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste URL here (e.g. https://youtu.be/...)")
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)

        # Quality & Format Selection
        self.quality_label = QLabel("Quality & Format")
        self.combo = QComboBox()
        self.combo.addItems([
            "Best Video + Audio (MP4)",
            "1080p (MP4)",
            "720p (MP4)",
            "Audio: MP3 (320kbps - Highest)",
            "Audio: M4A / AAC (Best Quality)",
            "Audio: FLAC (Lossless Audio)",
            "Audio: OPUS (Best Web Codec)"
        ])
        self.combo.setCurrentText(self.saved_quality)
        self.combo.currentTextChanged.connect(lambda t: self.settings.setValue("selected_quality", t))
        layout.addWidget(self.quality_label)
        layout.addWidget(self.combo)

        # Cookies
        cookie_layout = QHBoxLayout()
        self.use_cookies = QCheckBox("Use Browser Cookies (Bypass restrictions):")
        self.use_cookies.setChecked(self.saved_use_cookies)
        self.use_cookies.stateChanged.connect(self.save_cookie_state)

        self.browser_combo = QComboBox()
        self.browser_combo.addItems(["firefox", "brave", "chrome", "chromium"])
        self.browser_combo.setCurrentText(self.saved_browser)
        self.browser_combo.currentTextChanged.connect(lambda b: self.settings.setValue("selected_browser", b))

        cookie_layout.addWidget(self.use_cookies)
        cookie_layout.addWidget(self.browser_combo)
        layout.addLayout(cookie_layout)

        # Folder Selection
        self.path_label = QLabel("Download Folder")
        layout.addWidget(self.path_label)

        path_layout = QHBoxLayout()
        self.path_display = QLineEdit(self.save_directory)
        self.path_display.setReadOnly(True)
        self.path_btn = QPushButton("Browse...")
        self.path_btn.clicked.connect(self.select_folder)
        path_layout.addWidget(self.path_display)
        path_layout.addWidget(self.path_btn)
        layout.addLayout(path_layout)

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Main Download Button
        self.download_btn = QPushButton("Download Media")
        self.download_btn.setObjectName("download_btn")
        self.download_btn.clicked.connect(self.start_download)
        layout.addWidget(self.download_btn)

        # Actions Layout (Play & Open Folder)
        action_layout = QHBoxLayout()
        self.play_btn = QPushButton("▶ Play Last File")
        self.play_btn.setObjectName("play_btn")
        self.play_btn.setEnabled(False)
        self.play_btn.clicked.connect(self.play_file)
        action_layout.addWidget(self.play_btn)

        self.folder_btn = QPushButton("📁 Open in Folder")
        self.folder_btn.setEnabled(False)
        self.folder_btn.clicked.connect(self.open_folder)
        action_layout.addWidget(self.folder_btn)
        layout.addLayout(action_layout)

        # Console Log
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(self.log_box)

        # Footer Credit
        footer_label = QLabel("ir-mb © 2026")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setStyleSheet("color: #484f58; font-size: 11px; margin-top: 2px;")
        layout.addWidget(footer_label)

        self.setLayout(layout)

    def save_cookie_state(self):
        val = "true" if self.use_cookies.isChecked() else "false"
        self.settings.setValue("use_cookies", val)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Download Directory", self.save_directory)
        if folder:
            self.save_directory = folder
            self.path_display.setText(self.save_directory)
            self.settings.setValue("save_path", self.save_directory)

    def parse_progress(self, text):
        if "[download] Destination:" in text:
            filepath = text.split("[download] Destination:", 1)[1].strip()
            self.last_downloaded_file = filepath
            if any(ext in text.lower() for ext in ['.m4a', '.webm', '.opus']) and self.download_stage == 0:
                self.download_stage = 1

        if "[Merger] Merging formats into" in text:
            filepath = text.split('[Merger] Merging formats into "', 1)[1].rstrip('"').strip()
            self.last_downloaded_file = filepath
            self.progress_bar.setValue(96)
            return

        if "[ExtractAudio] Destination:" in text:
            filepath = text.split("[ExtractAudio] Destination:", 1)[1].strip()
            self.last_downloaded_file = filepath
            self.progress_bar.setValue(96)
            return

        match = re.search(r'\[download\]\s+(\d{1,3}(?:\.\d+)?)%', text)
        if match:
            percent = float(match.group(1))
            if "Audio:" in self.combo.currentText():
                calculated = int(percent)
            else:
                if self.download_stage == 0:
                    calculated = int(percent * 0.80)
                else:
                    calculated = int(80 + (percent * 0.16))

            if calculated > self.progress_bar.value():
                self.progress_bar.setValue(calculated)

    def start_download(self):
        url = self.url_input.text().strip()
        if not url:
            self.log_box.append("⚠️ Please provide a YouTube link.")
            return

        self.download_btn.setEnabled(False)
        self.play_btn.setEnabled(False)
        self.folder_btn.setEnabled(False)
        self.progress_bar.setValue(0)
        self.download_stage = 0
        self.last_downloaded_file = None
        self.log_box.clear()
        self.log_box.append("⚡ Connecting to yt-dlp...")

        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

        args = [
            "--newline",
            "-P", self.save_directory,
            "-o", "%(title)s.%(ext)s",
            "--no-mtime",
            "--extractor-args", "youtube:player_client=android,web,web_safari"
        ]

        if self.use_cookies.isChecked():
            args.extend(["--cookies-from-browser", self.browser_combo.currentText()])

        quality = self.combo.currentText()
        if quality == "Best Video + Audio (MP4)":
            args += ["-f", "bv*+ba/b", "--merge-output-format", "mp4"]
        elif quality == "1080p (MP4)":
            args += ["-f", "bv*[height<=1080]+ba/b[height<=1080]", "--merge-output-format", "mp4"]
        elif quality == "720p (MP4)":
            args += ["-f", "bv*[height<=720]+ba/b[height<=720]", "--merge-output-format", "mp4"]
        elif quality == "Audio: MP3 (320kbps - Highest)":
            args += ["-x", "--audio-format", "mp3", "--audio-quality", "0"]
        elif quality == "Audio: M4A / AAC (Best Quality)":
            args += ["-x", "--audio-format", "m4a"]
        elif quality == "Audio: FLAC (Lossless Audio)":
            args += ["-x", "--audio-format", "flac"]
        elif quality == "Audio: OPUS (Best Web Codec)":
            args += ["-x", "--audio-format", "opus"]

        args.append(url)
        self.process.start("yt-dlp", args)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode("utf-8", errors="ignore")
        for line in data.splitlines():
            line_str = line.strip()
            if line_str:
                self.parse_progress(line_str)
                self.log_box.append(line_str)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode("utf-8", errors="ignore")
        for line in data.splitlines():
            line_str = line.strip()
            if line_str:
                self.log_box.append(f"⚠️ {line_str}")

    def process_finished(self):
        if self.process.exitCode() == 0:
            self.progress_bar.setValue(100)
            self.log_box.append("\n✅ Download completed successfully!")
            self.play_btn.setEnabled(True)
            self.folder_btn.setEnabled(True)
        else:
            self.log_box.append("\n❌ Download failed or was interrupted.")
        self.download_btn.setEnabled(True)

    def play_file(self):
        if self.last_downloaded_file and os.path.exists(self.last_downloaded_file):
            subprocess.Popen(["xdg-open", self.last_downloaded_file])
        else:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.save_directory))

    def open_folder(self):
        if self.last_downloaded_file and os.path.exists(self.last_downloaded_file):
            subprocess.Popen(["xdg-open", os.path.dirname(self.last_downloaded_file)])
        else:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.save_directory))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec())
