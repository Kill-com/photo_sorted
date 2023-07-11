from PyQt5.QtWidgets import QDialog, QLabel, QPushButton, QHBoxLayout,QVBoxLayout,QGridLayout, QFileDialog,QComboBox
from PyQt5.sip import delete
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from .form_handler import handler
from sys import path
path.append("..")

from cancel import verev_dir, notJPG

class Win(QDialog):
    def __init__(self,MainW):
        super().__init__(MainW)
        self.mainW = MainW
        self.window()
        self.path_start_directory = None
    def window(self):

        title = QLabel()
        title.setText("Добро пожаловать!")
        title.setFont(QFont('Serif', 15, QFont.Light))
        title.setAlignment(Qt.AlignCenter)

        title2 = QLabel()
        title2.setText("Эта прорамма изменит размер, под печать,\nВсех ваших фотографии в папке")
        title2.setFont(QFont('Serif', 14, QFont.Light))
        title2.setAlignment(Qt.AlignHCenter)

        self.form = QComboBox()
        items = [" ","10x15","15x20","20x30"]
        self.form.addItems(items)

        form_text = QLabel()
        form_text.setText("1.Выберете под какую печать изменять фотографии")
        form_text.setFont(QFont('Serif', 12))
        form_text.setAlignment(Qt.AlignCenter)

        start_browse_text = QLabel()
        start_browse_text.setText("2.Выберете папку с фотографиями")
        start_browse_text.setFont(QFont('Arial', 11))
        start_browse_text.setAlignment(Qt.AlignCenter)

        start_browse = QPushButton()
        start_browse.setText("Выберете корневую папку:")
        start_browse.clicked.connect(self.collect_start_browse)

        self.label_start_browse = QLabel()
        self.label_start_browse.setFont(QFont('Arial', 11))
        self.label_start_browse.setAlignment(Qt.AlignCenter)

        cancel_button = QPushButton()
        cancel_button.setText("Назад")
        cancel_button.clicked.connect(self.cancel_def)

        confrim_button = QPushButton()
        confrim_button.setText("Подтвердить")
        confrim_button.clicked.connect(self.confrim_def)

        CC_layout = QHBoxLayout()
        CC_layout.addWidget(cancel_button)
        CC_layout.addWidget(confrim_button)

        layout_title=QVBoxLayout()
        layout_title.addWidget(title)
        layout_title.addWidget(title2)

        layout_brose_path = QVBoxLayout()
        layout_brose_path.addWidget(start_browse_text)
        layout_brose_path.addWidget(start_browse)
        layout_brose_path.addWidget(self.label_start_browse)

        layout_form = QVBoxLayout()
        layout_form.addWidget(form_text)
        layout_form.addWidget(self.form)

        layout_end = QVBoxLayout()
        layout_end.addLayout(layout_title)
        layout_end.addLayout(layout_form)
        layout_end.addLayout(layout_brose_path)
        layout_end.addLayout(CC_layout)

        self.mainW.setLayout(layout_end)
        self.mainW.show()

        self.item = [title,title2,self.form,form_text,start_browse,start_browse_text,self.label_start_browse,cancel_button,confrim_button]
    def collect_start_browse(self):
        self.mainW.setEnabled(False)
        start_directory = "C:/Users/User/Desktop"
        self.path_start_directory = QFileDialog.getExistingDirectory(None, "Выбрать папку", start_directory)
        ya = verev_dir.iz(self,main_Window=self, dirlist=self.path_start_directory,x = 1)
        if ya == 1:
            self.label_start_browse.setText(self.path_start_directory)
        else:
            self.path_start_directory= None
        self.mainW.setEnabled(True)
    def cancel_def(self):
        for item in self.item:
            item.deleteLater()
            del(item)
        delete(self.mainW.layout())
        self.mainW.createlayout()
    def confrim_def(self):
        if self.path_start_directory is not None and self.form.currentText() != " ":
            if self.form.currentText() == "10x15":
                form = 1
            elif self.form.currentText() == "15x20":
                form = 2
            elif self.form.currentText() == "20x30":
                form = 3
            a, directory = handler(file_path=self.path_start_directory, form = form)
            if a == 1:
                window = end_Win(directory=directory, mainW = self.mainW)
            elif a == 2:
                self.mainW.setEnabled(False)
                window = notJPG()
                window.exec()
                self.mainW.setEnabled(True)
        elif self.path_start_directory is None:
            window = error(1)
        elif self.form.currentText() == " ":
            window = error(2)
        elif self.path_start_directory is None and self.form.currentText() == " ":
            window = error(3)
        if window is not None:
            window.show()
            window.exec()
class error(QDialog):
    def __init__(self, x):
        super().__init__()
        self.setGeometry(300,250,10,10)
        title = QLabel()
        if x == 1:
            title.setText("Вы не выбрали коренную папку")
            self.windowTitle("Нету папки")
        if x == 2:
            title.setText("Вы не выбрали формат фото")
            self.setWindowTitle("Формат!")
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
class end_Win(QDialog):
    def __init__(self,directory, mainW):
        super().__init__()
        self.mainW = mainW
        self.mainW.setEnabled(False)
        self.setGeometry(300,250,10,10)
        title = QLabel()
        title.setText(f"Все готово, файлы были переданны в дерикторию:\n{directory}")
        self.setWindowTitle("Мы закончили")
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