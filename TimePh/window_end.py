from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.sip import delete
from sys import path
from html import *

path.append('..')
from cancel import clear

class window_end_W(QDialog):
    def __init__(self, main_window, widget_list):
        super().__init__()
        self.main_window = main_window
        title = QLabel()
        title.setText("""<p style='text-align: center; font-size: 15px; font-weight: bold; font-family: 
Arial, sans-serif;'>Все ваши файлы успешно заняли свое место!</p>""")
        title.setAlignment(Qt.AlignCenter)

        cancel = QPushButton(self)
        cancel.setText("Назад")
        cancel.clicked.connect(self.main_window.back)

        layout = QGridLayout()
        layout.addWidget(title, 0,0)
        layout.addWidget(cancel,1,0)
        main_window.widget_list = [main_window.browse, main_window.browse_edit_text]
        clear(self = self.main_window,x=1 , widget_list2=main_window.widget_list)

        self.main_window.setGeometry(300,250,10,10)
        self.main_window.setLayout(layout)
        self.main_window.show()
class not_photo(QDialog):
    def __init__(self, main_window, widget_list):
        super().__init__()
        self.widget_list = widget_list
        self.main_window = main_window
        self.setWindowTitle("Нету разницы")

        title = QLabel()
        title.setText("В папке найдена только одна фотосессия")

        cancel = QPushButton()
        cancel.setText("Назад")
        cancel.clicked.connect(self.cancel_def)

        layout = QGridLayout()
        layout.addWidget(title,0,0)
        layout.addWidget(cancel,1,0)

        self.setLayout(layout)
        self.show()

    def cancel_def(self):
        self.accept()
        self.main_window.setEnabled(True)
        self.main_window.back(x=1)
        
    