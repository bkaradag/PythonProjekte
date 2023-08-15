import sys
import sqlite3
from PyQt5 import QtWidgets


class Program(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.connection()
        self.init_ui()

    def connection(self):
        conn = sqlite3.connect("database.db")

        self.cursor = conn.cursor()
        self.cursor.execute("CREATE TABLE If NOT EXISTS Users (username TEXT,password TEXT)")

        conn.commit()

    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.einloggen = QtWidgets.QPushButton("Einloggen")
        self.text = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text)
        v_box.addStretch()
        v_box.addWidget(self.einloggen)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.einloggen.clicked.connect(self.login)

        self.setWindowTitle("Anmelden")

        self.show()

    def login(self):
        name = self.username.text()
        passw = self.password.text()

        self.cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (name, passw))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.text.setText("User nicht existiert.")
        else:
            self.text.setText("Wilkommen " + name)


app = QtWidgets.QApplication(sys.argv)

program = Program()

sys.exit(app.exec_())
