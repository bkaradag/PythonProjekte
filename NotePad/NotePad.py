"""
NotePad
"""
import sys
import os

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout
from PyQt5.QtWidgets import QAction, qApp, QMainWindow


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
        folder_name = QFileDialog.getOpenFileName(self, "Öffnen", os.getenv("Desktop"))

        with open(folder_name[0], "r") as file:
            self.text_in.setText(file.read())

    def data_save(self):
        folder_name = QFileDialog.getSaveFileName(self, "Speichern", os.getenv("Desktop"))

        with open(folder_name[0], "w") as file:
            file.write(self.text_in.toPlainText())


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.fenster = Notepad()

        self.setCentralWidget(self.fenster)

        self.menu_erstellen()

    def menu_erstellen(self):

        menu_bar = self.menuBar()

        folder = menu_bar.addMenu("Folder")

        folder_open = QAction("Öffnen",self)
        folder_open.setShortcut("Ctrl+O")

        data_save = QAction("Speichern",self)
        data_save.setShortcut("Ctrl+S")

        clear_text = QAction("Löschen",self)
        clear_text.setShortcut("Ctrl+D")

        exit = QAction("Beenden",self)
        exit.setShortcut("Ctrl+Q")

        folder.addAction(folder_open)
        folder.addAction(data_save)
        folder.addAction(clear_text)
        folder.addAction(exit)

        folder.triggered.connect(self.response)

        bearbeiten = menu_bar.addMenu("Bearbeiten")

        self.show()

    def response(self,action):
        if action.text() == "Öffnen":
            self.fenster.folder_open()
        elif action.text() == "Speichern":
            self.fenster.data_save()
        elif action.text() == "Löschen":
            self.fenster.clear_text()
        elif action.text() == "Beenden":
            qApp.quit()


app = QApplication(sys.argv)

notepad = Notepad()

sys.exit(app.exec_())
