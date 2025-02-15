import sys
import json
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QCheckBox, QPushButton, QLabel, QMessageBox, QComboBox, QGridLayout, QDialog
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize


class AboutDeveloperDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("حول المطور")
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet("background-color: #e6f7ff;")

        # Main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Developer Info
        developer_label = QLabel("المطور: محمد الباقر")
        developer_label.setFont(QFont("Arial", 14, QFont.Bold))
        developer_label.setStyleSheet("color: #34495e;")
        developer_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(developer_label)

        # About the Program
        about_label = QLabel(
            "هذا البرنامج مخصص لتعزيز أمان النظام عن طريق تعطيل أو تمكين بعض الإعدادات."
        )
        about_label.setFont(QFont("Arial", 12))
        about_label.setStyleSheet("color: #2c3e50;")
        about_label.setWordWrap(True)
        about_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(about_label)

        # Social Media Icons
        icon_layout = QHBoxLayout()
        icon_layout.setAlignment(Qt.AlignCenter)

        telegram_button = QPushButton()
        telegram_button.setIcon(QIcon("telegram.png"))  # Use relative path
        telegram_button.setIconSize(QSize(30, 30))
        telegram_button.setStyleSheet("border: none;")
        telegram_button.setToolTip("Contact on Telegram")
        telegram_button.clicked.connect(lambda: webbrowser.open("https://t.me/r94xs"))
        icon_layout.addWidget(telegram_button)

        instagram_button = QPushButton()
        instagram_button.setIcon(QIcon("instagram.png"))  # Use relative path
        instagram_button.setIconSize(QSize(30, 30))
        instagram_button.setStyleSheet("border: none;")
        instagram_button.setToolTip("Contact on Instagram")
        instagram_button.clicked.connect(lambda: webbrowser.open("https://instagram.com/wsl.iq"))
        icon_layout.addWidget(instagram_button)

        main_layout.addLayout(icon_layout)

        # Close Button
        close_button = QPushButton("إغلاق")
        close_button.setStyleSheet(
            "background-color: #e74c3c; color: white; font-size: 16px; padding: 10px; border-radius: 10px;"
        )
        close_button.clicked.connect(self.close)
        main_layout.addWidget(close_button)


def run_hardening_tool():
    class HardeningTool(QMainWindow):
        SETTINGS_FILE = "hardening_settings.json"

        def __init__(self):
            super().__init__()
            self.setWindowTitle("Hardening Tool")
            self.setGeometry(200, 200, 800, 600)
            self.setStyleSheet("background-color: #e6f7ff;")

            # Main container widget
            container = QWidget()
            self.setCentralWidget(container)

            # Main layout
            main_layout = QVBoxLayout()
            container.setLayout(main_layout)

            # About Developer Button
            about_button = QPushButton("حول المطور")
            about_button.setStyleSheet(
                "background-color: #3498db; color: white; font-size: 16px; padding: 10px; border-radius: 10px;"
            )
            about_button.clicked.connect(self.show_about_developer)
            main_layout.addWidget(about_button, alignment=Qt.AlignRight)

            # Language Selection
            language_layout = QHBoxLayout()
            language_label = QLabel("")
            language_label.setFont(QFont("Arial", 15, QFont.Bold))
            language_label.setStyleSheet("color: #2c3e50;")

            self.language_selector = QComboBox()
            self.language_selector.addItems(["English", "العربية"])
            self.language_selector.setStyleSheet(
                "background-color: #ffffff; color: #2c3e50; font-size: 14px; padding: 5px; border-radius: 5px;"
            )
            self.language_selector.currentIndexChanged.connect(self.change_language)

            language_layout.addWidget(language_label)
            language_layout.addWidget(self.language_selector)
            main_layout.addLayout(language_layout)

            # Header Label
            self.header = QLabel("Hardening Tool - Enhance Your Security")
            self.header.setFont(QFont("Arial", 18, QFont.Bold))
            self.header.setAlignment(Qt.AlignCenter)
            self.header.setStyleSheet("color: #1a5276; padding: 10px;")
            main_layout.addWidget(self.header)

            self.checkboxes = {}
            self.translations = {
                "Windows Script Host": "مضيف سكربت ويندوز",
                "Office Packager Objects (OLE)": "كائنات حزمة الأوفيس (OLE)",
                "Office Macros": "ماكرو الأوفيس",
                "Office ActiveX": "أكتيف إكس الأوفيس",
                "Office DDE Mitigations": "تخفيفات DDE للأوفيس",
                "Acrobat Reader JavaScript": "جافاسكربت قارئ أكروبات",
                "Acrobat Reader Embedded Objects": "الكائنات المدمجة في قارئ أكروبات",
                "Acrobat Reader Protected Mode": "الوضع المحمي لقارئ أكروبات",
                "Acrobat Reader Protected View": "العرض المحمي لقارئ أكروبات",
                "Acrobat Reader Enhanced Security": "الأمان المحسن لقارئ أكروبات",
                "Show File Extensions": "إظهار امتدادات الملفات",
                "AutoRun and AutoPlay": "التشغيل التلقائي وتشغيل الوسائط",
                "Disable Powershell": "تعطيل PowerShell",
                "Disable cmd.exe": "تعطيل cmd.exe",
                "User Account Control": "التحكم بحساب المستخدم",
                "File associations": "ارتباطات الملفات",
                "Windows ASR rules": "قواعد ASR لويندوز",
                "LSA Protection": "حماية LSA",
                "Defender PUA Protection": "حماية Defender ضد التطبيقات غير المرغوب بها"
            }

            options = list(self.translations.keys())
            self.load_settings()

            grid_layout = QGridLayout()
            row, col = 0, 0
            for option in options:
                checkbox = QCheckBox(option)
                checkbox.setStyleSheet(
                    "font-size: 14px; color: #154360; background-color: #d6eaf8; padding: 5px; border-radius: 5px;"
                )
                self.checkboxes[option] = checkbox
                checkbox.setChecked(self.settings.get(option, False))
                checkbox.stateChanged.connect(lambda state, opt=option: self.update_button_label(opt))
                grid_layout.addWidget(checkbox, row, col)
                col += 1
                if col > 2:  # 3 checkboxes per row
                    col = 0
                    row += 1
            main_layout.addLayout(grid_layout)

            self.harden_button = QPushButton("Harden")
            self.harden_button.setStyleSheet(
                "background-color: #1abc9c; color: white; font-size: 16px; padding: 10px; border-radius: 10px;"
            )
            self.harden_button.clicked.connect(self.harden_system)
            main_layout.addWidget(self.harden_button)

            save_exit_button = QPushButton("Save & Exit")
            save_exit_button.setStyleSheet(
                "background-color: #e74c3c; color: white; font-size: 16px; padding: 10px; border-radius: 10px;"
            )
            save_exit_button.clicked.connect(self.save_and_exit)
            main_layout.addWidget(save_exit_button)

            self.update_all_button_labels()

        def show_about_developer(self):
            """Show the About Developer dialog."""
            dialog = AboutDeveloperDialog()
            dialog.exec_()

        def load_settings(self):
            """Load settings from the JSON file."""
            try:
                with open(self.SETTINGS_FILE, "r") as file:
                    self.settings = json.load(file)
            except FileNotFoundError:
                self.settings = {}

        def save_settings(self):
            """Save current settings to the JSON file."""
            self.settings = {option: checkbox.isChecked() for option, checkbox in self.checkboxes.items()}
            with open(self.SETTINGS_FILE, "w") as file:
                json.dump(self.settings, file, indent=4)

        def update_button_label(self, option):
            """Update the button label based on checkbox state."""
            enabled_options = [opt for opt, cb in self.checkboxes.items() if cb.isChecked()]
            if enabled_options:
                self.harden_button.setText(f"Harden {len(enabled_options)} Options")
            else:
                self.harden_button.setText("Harden")

        def update_all_button_labels(self):
            """Update the harden button label for all options."""
            self.update_button_label(None)

        def harden_system(self):
            """Execute the hardening operations based on selected options."""
            enabled_options = [option for option, checkbox in self.checkboxes.items() if checkbox.isChecked()]

            if enabled_options:
                message = "The following settings have been hardened:\n" + "\n".join(enabled_options)
                self.execute_commands(enabled_options)
            else:
                message = "No options selected for hardening."

            QMessageBox.information(self, "Hardening Summary", message)

        def execute_commands(self, options):
            """Placeholder for executing hardening commands."""
            for option in options:
                print(f"Executing hardening for: {option}")

        def save_and_exit(self):
            """Save the settings and exit the application."""
            self.save_settings()
            QMessageBox.information(self, "Save Settings", "Settings have been saved successfully!")
            self.close()

        def change_language(self):
            """Change the language of the interface."""
            selected_language = self.language_selector.currentText()
            if selected_language == "العربية":
                self.setWindowTitle("أداة تعزيز الأمان")
                self.header.setText("أداة تعزيز الأمان - عزز أمانك")
                for option, checkbox in self.checkboxes.items():
                    checkbox.setText(self.translations[option])
                self.harden_button.setText("تعطيل")
            else:
                self.setWindowTitle("Hardening Tool")
                self.header.setText("Hardening Tool - Enhance Your Security")
                for option, checkbox in self.checkboxes.items():
                    checkbox.setText(option)
                self.harden_button.setText("Harden")

    app = QApplication(sys.argv)
    window = HardeningTool()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    run_hardening_tool()