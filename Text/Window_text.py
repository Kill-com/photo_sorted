from PyQt5.QtWidgets import QDialog, QLabel,QPushButton, QVBoxLayout, QTextEdit, QHBoxLayout, QFileDialog, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from html import *
from PyQt5.sip import delete

from sys import path

from .text_handler import text_handler_def
path.append("..")
from cancel import verev_dir, clear
class window_text(QDialog):
    def __init__(self, mainW):
        super().__init__()
        window_text.mainW = mainW
        self.time_window()
        window_text.path_directory = None
        window_text.URL_tabel = None
    def time_window(self):
        
        font_title = QFont('Serif', 15, QFont.Light)
        font_text = QFont('Serif', 11, QFont.Light)

        title = QLabel()
        title.setText("Добро пожаловать в программу:\nРазделение фотографии по номерам")
        title.adjustSize()
        title.setFont(font_title)
        title.setAlignment(Qt.AlignCenter)

        text = QLabel()
        text.setText("""<p style='text-align: center;font-size: 20px;font-family: Georgia, serif;'>
!Выберете все нужные файлы!</p>""")
        text.setAlignment(Qt.AlignHCenter)

        self.browse_directory = QPushButton()
        self.browse_directory.setText("Выбрать корневую папку:")
        self.browse_directory.clicked.connect(window_text.collect_directory_dirlist)
        self.browse_directory.setFont(font_text)

        label_browse_directory = QLabel()
        label_browse_directory.setFont(QFont('Arial', 11))
        label_browse_directory.setAlignment(Qt.AlignCenter)
        window_text.browse_edit_text = label_browse_directory

        directory_layout = QVBoxLayout()
        directory_layout.addWidget(self.browse_directory)
        directory_layout.addWidget(label_browse_directory)

        browse_Text_File = QLabel()
        browse_Text_File.setText("Напишите ссылку на гугл таблицы:")
        browse_Text_File.setFont(font_text)
        browse_Text_File.setAlignment(Qt.AlignCenter)

        window_text.label_browse_Text_File = QTextEdit()
        window_text.label_browse_Text_File.setFont(QFont('Arial', 11))
        window_text.label_browse_Text_File.setAlignment(Qt.AlignCenter)

        browse_num_tabel = QLabel()
        browse_num_tabel.setText("Напишите номер столбца:\n(Или несколько, через пробел)")
        browse_num_tabel.setFont(font_text)
        browse_num_tabel.setAlignment(Qt.AlignCenter)

        window_text.label_browse_num_tabel = QTextEdit()
        window_text.label_browse_num_tabel.setFont(QFont('Arial', 11))
        window_text.label_browse_num_tabel.setAlignment(Qt.AlignCenter)

        browse_label_sheet = QLabel()
        browse_label_sheet.setText("Напишите номер листа:\n(По умолчанию 1)")
        browse_label_sheet.setFont(font_text)
        browse_label_sheet.setAlignment(Qt.AlignCenter)

        window_text.label_browse_sheet = QTextEdit()
        window_text.label_browse_sheet.setFont(QFont('Arial', 11))
        window_text.label_browse_sheet.setAlignment(Qt.AlignCenter)

        layout_label_text = QGridLayout()
        layout_label_text.addWidget(browse_Text_File,0,0)
        layout_label_text.addWidget(window_text.label_browse_Text_File,1,0,3,1)
        layout_label_text.addWidget(browse_num_tabel,0,1)
        layout_label_text.addWidget(window_text.label_browse_num_tabel,1,1)
        layout_label_text.addWidget(browse_label_sheet, 2,1)
        layout_label_text.addWidget(window_text.label_browse_sheet,3,1)

        cancel_button = QPushButton()
        cancel_button.setText("Назад")
        cancel_button.clicked.connect(window_text.cancel_def)

        confrim_button = QPushButton()
        confrim_button.setText("Подтвердить")
        confrim_button.clicked.connect(window_text.confrim_def)

        noterror = QLabel()
        noterror.setText("""<p style="text-align: center;font-size: 20px;font-family: Georgia, serif;">
Внимание, ссылку надо брать с настроек доступа</p>""")
        noterror.setAlignment(Qt.AlignHCenter)

        CC_layout = QHBoxLayout()
        CC_layout.addWidget(cancel_button)
        CC_layout.addWidget(confrim_button)

        end_layout = QVBoxLayout()
        end_layout.addWidget(title)
        end_layout.addWidget(text)
        end_layout.addLayout(directory_layout)
        end_layout.addWidget(noterror)
        end_layout.addLayout(layout_label_text)
        end_layout.addLayout(CC_layout)

        self.mainW.setLayout(end_layout)
        self.mainW.show()
        window_text.item = [title,text,self.browse_directory,label_browse_directory,
        browse_Text_File,window_text.label_browse_Text_File,browse_num_tabel,window_text.label_browse_num_tabel,
        browse_label_sheet, window_text.label_browse_sheet,noterror,cancel_button,confrim_button]
    def collect_directory_dirlist(self):
        window_text.mainW.setEnabled(False)
        window_text.path_directory = QFileDialog.getExistingDirectory(None, "Выбрать папку", "C:/Users/User/Desktop")
        ya = verev_dir.iz(self,main_Window=self, dirlist=window_text.path_directory,x = 1)
        if ya == 1:
            window_text.browse_edit_text.setText(window_text.path_directory)
        else:
            window_text.path_directory = None
        window_text.mainW.setEnabled(True)
        
    def cancel_def(self):
        for item in window_text.item:
            item.deleteLater()
            del(item)
        delete(window_text.mainW.layout())
        window_text.mainW.createlayout()
    def confrim_def(self):
        window = None
        URL_tabel = window_text.label_browse_Text_File.toPlainText()
        num_tabel = window_text.label_browse_num_tabel.toPlainText()
        google_sheet = window_text.label_browse_sheet.toPlainText()
        if google_sheet.strip() == '':
            google_sheet = 0
        else:
            google_sheet = int(google_sheet) - 1
        if window_text.path_directory and URL_tabel and num_tabel is not None:
            window_text.mainW.setEnabled(False)
            text_handler_def(path_directory=window_text.path_directory,
            URL_tabel=URL_tabel, num_tabel=num_tabel, google_sheet=google_sheet,
            main_window=window_text.mainW)
        elif window_text.path_directory and URL_tabel is not None:
            window = notpath(x = 3)
        elif window_text.path_directory and num_tabel is not None:
            window = notpath(x = 5)
        elif num_tabel and URL_tabel is not None:
            window =notpath(x = 6)
        elif num_tabel is not None:
            window = notpath(x = 7)
        elif window_text.path_directory is not None:
            window = notpath(x = 1)
        elif URL_tabel is not None:
            window = notpath(x = 2)
        else:
            window = notpath(x = 4)
        if window is not None:
            window.show()
            window.exec()

class notpath(QDialog):
    def __init__(self, x):
        super().__init__()
        window_text.mainW.setEnabled(False)
        self.setGeometry(300,250,10,10)
        title = QLabel()
        if x == 1:
            self.setWindowTitle("Нету файла")
            title.setText("Вы не написали ссылку и номер столбца!")
        elif x == 2:
            self.setWindowTitle("Нету папки")
            title.setText("Вы не выбрали корневую папку и номер столбца!")
        elif x == 3:
            self.setWindowTitle("Нету столбца")
            title.setText("Вы не выбрали номер столбца")
        elif x == 4:
            self.setWindowTitle("Нету всего")
            title.setText("Вы не выбрали вообще все!")
        elif x == 5:
            self.setWindowTitle("Нету ссылки")
            title.setText("Вы не написали ссылку!")
        elif x == 6:
            self.setWindowTitle("Нету папки")
            title.setText("Вы не выбрали корневую папку!")
        elif x == 7:
            self.setWindowTitle("Нету чего то")
            title.setText("Вы не выбрали корневую папку и ссылку!")
        title.setFont(QFont('Serif', 15, QFont.Light))

        close_button = QPushButton()
        close_button.setText("Хорошо...")
        close_button.clicked.connect(self.close_def)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(close_button)

        self.setLayout(layout)
    def close_def(self):
        self.accept()
        window_text.mainW.setEnabled(True)
class end_text(QDialog):
    def __init__(self,directory):
        super().__init__()
        self.directory = directory

        self.window()
    def window(self):
        self.setGeometry(300,250,10,10)
        self.setWindowTitle("Мы закончили")
        font = QFont('Serif', 11, QFont.Light)
        title_end = QLabel()
        title_end.setText(f"Все готово, файлы были переданны в дерикторию:\n{self.directory}")
        title_end.setFont(font)

        close_button = QPushButton()
        close_button.setText("Хорошо...")
        close_button.clicked.connect(self.close_def)

        layout = QVBoxLayout()
        layout.addWidget(title_end)
        layout.addWidget(close_button)

        self.setLayout(layout)
        self.show()
    def close_def(self):
        self.accept()
        window_text.mainW.setEnabled(True)
        window_text.cancel_def(window_text.mainW)



