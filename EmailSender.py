import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.to = QLabel("To: ")
        self.to_text = QLineEdit()
        self.subj = QLabel("Subject: ")
        self.subj_text = QLineEdit()
        self.senden_button = QPushButton("Senden")
        self.text_loeschen = QPushButton("Text Löschen")
        self.email = QLabel("Email: ")
        self.mail_text = QTextEdit()
        self.tage = QLabel("Tage: ")
        self.checkbox = QCheckBox("Montag")
        self.checkbox2 = QCheckBox("Dienstag")
        self.checkbox3 = QCheckBox("Mittwoch")
        self.checkbox4 = QCheckBox("Donnerstag")
        self.checkbox5 = QCheckBox("Freitag")

        h_box = QHBoxLayout()
        h_box.addWidget(self.to)
        h_box.addWidget(self.to_text)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.email)
        h_box2.addWidget(self.mail_text)

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.senden_button)
        h_box3.addWidget(self.text_loeschen)

        h_box4 = QVBoxLayout()
        h_box4.addStretch()
        h_box4.addWidget(self.tage)
        h_box4.addWidget(self.checkbox)
        h_box4.addWidget(self.checkbox2)
        h_box4.addWidget(self.checkbox3)
        h_box4.addWidget(self.checkbox4)
        h_box4.addWidget(self.checkbox5)

        h_box5 = QHBoxLayout()
        h_box5.addWidget(self.subj)
        h_box5.addWidget(self.subj_text)

        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addLayout(h_box5)
        v_box.addStretch()
        v_box.addLayout(h_box2)
        v_box.addStretch()
        v_box.addLayout(h_box4)
        v_box.addStretch()
        v_box.addLayout(h_box3)
        v_box.addStretch()

        self.to_text.setFixedSize(450, 30)
        self.subj_text.setFixedSize(450, 30)
        self.mail_text.setFixedSize(450, 450)

        self.setLayout(v_box)

        self.setGeometry(400, 100, 300, 300)
        self.setFixedSize(600, 900)

        self.setWindowTitle("Mail Senden")

        self.senden_button.clicked.connect(self.mail_senden)
        # self.senden_button.clicked.connect(lambda : self.mail_senden(self.checkbox.isChecked(), self.mail_text))
        self.text_loeschen.clicked.connect(self.loeschen)
        self.show()

    def mail_senden(self,checked):
        try:
            msg = MIMEMultipart()
            msg["From"] = "your_email@gmail.com"
            msg["To"] = self.to_text.text()
            msg["Subject"] = self.subj_text.text()


            text = self.mail_text.toPlainText()
            text2 = "Ich kann an den Tagen arbeiten, die ich für diese Woche markiert habe:"
            text3 = "Sehr geehrte Damen und Herren,\n"
            text4 = "\nMit freundlichen Grüßen\n Berkay Karadag"

            # markierte_tage = [] TODO: buraya bakilmasi gerekiyor. Secilen günleri de mail metnine eklemesi gerekiyor.
            #
            # if self.checkbox.isChecked():
            #     markierte_tage.append(self.checkbox.text())
            # if self.checkbox2.isChecked():
            #     markierte_tage.append(self.checkbox2.text())
            # if self.checkbox3.isChecked():
            #     markierte_tage.append(self.checkbox3.text())
            # if self.checkbox4.isChecked():
            #     markierte_tage.append(self.checkbox4.text())
            # if self.checkbox5.isChecked():
            #     markierte_tage.append(self.checkbox5.text())
            #
            # if markierte_tage:
            #     text_tag = "Ich kann an den Tagen arbeiten, die ich für diese Woche markiert habe:\n"
            #     markierte_tage += "\n".join(markierte_tage)
            #     self.mail_text.append(text_tag)

            msg_bd = MIMEText(text3 + text + text2 + text4, "plain")
            msg.attach(msg_bd)

            mail = smtplib.SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("bk6991@gmail.com", "vosjyyoovzbvmous")
            mail.sendmail(msg["From"], msg["To"], msg.as_string())

            print("Mail wurde erfolgreich gesendet!")
            mail.quit()
        except Exception as e:
            print("Ein Fehler aufgetreten:", str(e))

    def loeschen(self):
        self.mail_text.clear()

    def click(self,checked):
        pass

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
