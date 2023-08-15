"""
NotePad
"""
import sys
import os

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout,QAction,qApp,QMainWindow

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menu_bar = self.menuBar()

        folder = menu_bar.addMenu("Folder")
        bearbeiten = menu_bar.addMenu("Bearbeiten")


class Notepad(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.text_in = QTextEdit()

        self.erase = QPushButton("Loeschen")
        self.open = QPushButton("Öffnen")
        self.save = QPushButton("Speichern")

        h_box = QHBoxLayout()

        h_box.addWidget(self.erase)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()

        v_box.addWidget(self.text_in)

        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle("NotePad")

        self.erase.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.folder_open)
        self.save.clicked.connect(self.data_save)

    def clear_text(self):
        self.text_in.clear()

    def folder_open(self):
        folder_name = QFileDialog.getOpenFileName(self, "Öffnen",
                                                  os.getenv("Desktop"))  # bilgiyarin yolunu söyler os.getenv

        with open(folder_name[0], "r") as file:
            self.text_in.setText(file.read())  # dosyanin icindekileri komple yazdirir.

    def data_save(self):
        folder_name = QFileDialog.getSaveFileName(self, "Speichern", os.getenv("Desktop"))

        with open(folder_name[0], "w") as file:
            file.write(self.text_in.toPlainText())  # tüm yazilari alip dosyaaya ekler.

        self.show()


app = QApplication(sys.argv)

notepad = Notepad()

sys.exit(app.exec_())
