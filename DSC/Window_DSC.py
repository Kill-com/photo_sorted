from PyQt5.QtWidgets import (QDialog, QLabel, QPushButton,QVBoxLayout, QFileDialog, QHBoxLayout,
QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.sip import delete
from os.path import dirname
from html import *
from sys import path
from .DSC_handler import DSC_handler_def
path.append("..")
from cancel import verev_dir, notJPG
class win_DSC(QDialog):
    def __init__(self, mainW):
        super().__init__(mainW)
        self.mainW = mainW
        self.start_window()
        self.path_DSC_directory = None
        self.path_start_directory = None
    def start_window(self):
        title = QLabel(self)
        title.setText("Добро пожаловать в программу:\nРазделения фотографии по времени")
        title.adjustSize()
        title.setFont(QFont('Serif', 15, QFont.Light))
        title.setAlignment(Qt.AlignHCenter)

        text = QLabel()
        text.setText("""<p style='text-align: center;font-size: 20px;font-family: Georgia, serif;'>
!Выберете все нужные файлы!</p>""")
        label_you_name = QLabel()
        label_you_name.setText("Напишите название папки(По желанию)")
        label_you_name.setFont(QFont('Serif', 11, QFont.Light))
        label_you_name.setAlignment(Qt.AlignCenter)

        self.you_name = QTextEdit()
        self.you_name.setFont(QFont('Serif', 11, QFont.Light))
        self.you_name.setFixedSize(480,40)
        self.you_name.setAlignment(Qt.AlignHCenter)
        

        start_browse = QPushButton()
        start_browse.setText("Выберете корневую папку:")
        start_browse.clicked.connect(self.collect_start_browse)

        label_start_browse = QLabel()
        label_start_browse.setFont(QFont('Arial', 11))
        label_start_browse.setAlignment(Qt.AlignCenter)
        self.label_start_browse = label_start_browse

        layout_start_browse = QVBoxLayout()
        layout_start_browse.addWidget(start_browse)
        layout_start_browse.addWidget(label_start_browse)

        DSC_browse = QPushButton()
        DSC_browse.setText("Выберете папку с DSC:")
        DSC_browse.clicked.connect(self.collect_DSC_browse)

        label_DSC_browse = QLabel()
        label_DSC_browse.setFont(QFont('Arial', 11))
        label_DSC_browse.setAlignment(Qt.AlignCenter)
        self.label_DSC_browse = label_DSC_browse

        layot_DSC_browse = QVBoxLayout()
        layot_DSC_browse.addWidget(DSC_browse)
        layot_DSC_browse.addWidget(label_DSC_browse)

        cancel_button = QPushButton()
        cancel_button.setText("Назад")
        cancel_button.clicked.connect(self.cancel_def)

        confrim_button = QPushButton()
        confrim_button.setText("Подтвердить")
        confrim_button.clicked.connect(self.confrim_def)

        CC_layout = QHBoxLayout()
        CC_layout.addWidget(cancel_button)
        CC_layout.addWidget(confrim_button)

        title_layout = QVBoxLayout()
        title_layout.addWidget(title)
        title_layout.addWidget(text)
        end_layout = QVBoxLayout()
        end_layout.addLayout(title_layout)
        end_layout.addWidget(label_you_name)
        end_layout.addWidget(self.you_name)
        end_layout.addLayout(layout_start_browse)
        end_layout.addLayout(layot_DSC_browse)
        end_layout.addLayout(CC_layout)

        self.mainW.setLayout(end_layout)
        self.mainW.show()

        self.item = [title,text,start_browse,label_start_browse,
        DSC_browse,label_DSC_browse,cancel_button,confrim_button,label_you_name, self.you_name]
    def collect_start_browse(self):
        self.mainW.setEnabled(False)
        start_directory = "C:/Users/User/Desktop"
        if self.path_DSC_directory is not None:
            start_directory = dirname(self.path_DSC_directory)
        self.path_start_directory = QFileDialog.getExistingDirectory(None, "Выбрать папку", start_directory)
        ya = verev_dir.iz(self,main_Window=self, dirlist=self.path_start_directory,x = 1)
        if ya == 1:
            self.label_start_browse.setText(self.path_start_directory)
        else:
            self.path_start_directory= None
        self.mainW.setEnabled(True)
    def collect_DSC_browse(self):
        self.mainW.setEnabled(False)
        start_directory = "C:/Users/User/Desktop"
        if self.path_start_directory is not None:
            start_directory = self.path_start_directory
        self.path_DSC_directory = QFileDialog.getExistingDirectory(None, "Выбрать папку", start_directory)
        ya = verev_dir.iz(self,main_Window=self, dirlist=self.path_DSC_directory,x = 1)
        if ya == 1:
            self.label_DSC_browse.setText(self.path_DSC_directory)
        else:
            self.path_DSC_directory= None
        self.mainW.setEnabled(True)
    def cancel_def(self):
        for item in self.item:
            item.deleteLater()
            del(item)
        delete(self.mainW.layout())
        self.mainW.createlayout()
    def confrim_def(self):
        window = None
        name = None
        if self.path_start_directory and self.path_DSC_directory is not None:
            name = self.you_name.toPlainText()
            if name is not None:
                a, directory = DSC_handler_def(path_start_directory=self.path_start_directory,
                path_DSC_directory=self.path_DSC_directory, you_directory= name)
            else:
                a, directory= DSC_handler_def(path_start_directory=self.path_start_directory,
                path_DSC_directory=self.path_DSC_directory)
            if a == 1:
                window_end = end_window(directory=directory, mainW=self.mainW)
                window_end.show()
                window_end.exec()
                self.cancel_def()
            elif a == 2:
                self.mainW.setEnabled(False)
                window = notJPG()
                window.exec()
                self.mainW.setEnabled(True)
            elif a == 3:
                window = new_directory()
                name = None
                self.you_name = None
        elif self.path_DSC_directory is not None:
            window = notpath(x=1)
        elif self.path_start_directory is not None:
            window = notpath(x=2)
        else:
            window = notpath(x=3)
        if window is not None:
            window.show()
            window.exec()
    
class notpath(QDialog):
    def __init__(self, x):
        super().__init__()
        self.setGeometry(300,250,10,10)
        title = QLabel()
        if x == 1:
            title.setText("Вы не выбрали коренную папку")
            self.windowTitle("Нету папки")
        if x == 2:
            title.setText("Вы не выбрали DSC папку")
            self.setWindowTitle("Нету DSC")
        if x == 3:
            self.setWindowTitle("Нету всего")
            title.setText("Вы не выбрали вообще все!")
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
class new_directory(QDialog):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,250,10,10)
        title = QLabel()
        title.setText("Папка должна быть пустой")
        self.setWindowTitle("Новая папка!!")
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
class end_window(QDialog):
    def __init__(self,directory, mainW):
        super().__init__()
        self.mainW = mainW
        self.mainW.setEnabled(False)
        self.setGeometry(300,250,10,10)
        title = QLabel()
        title.setText(f"Все готово, файлы были переданны в дерикторию:\n{directory}")
        self.setWindowTitle("Мы закончили!")
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
        self.mainW.setEnabled(True)
        