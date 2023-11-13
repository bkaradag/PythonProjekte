import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QPushButton, QTextEdit, QListWidget, QLabel, QWidget, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import fitz
import glob

class PDFReaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Reader")
        self.setGeometry(100, 100, 1000, 800)

        self.init_ui()

    def init_ui(self):
        # Widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.file_list_widget = QListWidget(self)
        self.text_pdf = QLabel("PDF Files: ")
        self.text_value_search = QLabel("Search Value: ")
        self.text_result = QLabel("Result: ")
        self.pdf_preview_label = QLabel(self)
        self.a_values_textedit = QTextEdit(self)
        self.a_values_textedit.setReadOnly(True)
        self.a_input = QLineEdit(self)

        # Layout
        main_layout = QHBoxLayout(self.central_widget)
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        right_layout.addWidget(self.text_pdf)
        right_layout.addWidget(self.file_list_widget)

        right_layout.addWidget(self.text_value_search)
        right_layout.addWidget(self.a_input)
        right_layout.addWidget(self.text_result)
        right_layout.addWidget(self.a_values_textedit)

        load_button = QPushButton("PDF File", self)
        load_button.clicked.connect(self.load_pdf_files)
        right_layout.addWidget(load_button)

        search_button = QPushButton("Search Value", self)
        search_button.clicked.connect(self.search_a_values)
        right_layout.addWidget(search_button)

        left_layout.addWidget(self.pdf_preview_label)

        # PDF Preview
        self.file_list_widget.itemClicked.connect(self.display_pdf_preview)


    def load_pdf_files(self):
        pdf_dir = QFileDialog.getExistingDirectory(self, "Select File")

        if pdf_dir:
            self.file_list_widget.clear()
            self.a_values_textedit.clear()

            pdf_files = glob.glob(pdf_dir + "/*.pdf")

            for pdf_file in pdf_files:
                self.file_list_widget.addItem(pdf_file)


    def display_pdf_preview(self, item):
        pdf_path = item.text()
        self.display_pdf_preview_image(pdf_path)

    def display_pdf_preview_image(self, pdf_path):
        doc = fitz.open(pdf_path)
        page = doc[0]

        pixmap = QPixmap()
        pixmap.loadFromData(page.get_pixmap().tobytes())
        self.pdf_preview_label.setPixmap(pixmap)

    def extract_a_values(self, pdf_path, search_term):
        a_values = []

        doc = fitz.open(pdf_path)

        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()

            # Search value
            a_values.extend(char.lower() for char in text if char == search_term.lower())

        doc.close()

        return a_values

    def search_a_values(self):
        selected_item = self.file_list_widget.currentItem()
        if selected_item:
            pdf_path = selected_item.text()
            search_term = self.a_input.text()

            if pdf_path and search_term:
                self.display_a_values(pdf_path, search_term)

    def display_a_values(self, pdf_path, search_term):
        a_values = self.extract_a_values(pdf_path, search_term)
        self.a_values_textedit.setPlainText("\n".join(a_values))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = PDFReaderApp()
    mainWin.show()
    sys.exit(app.exec_())
