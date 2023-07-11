from PyQt5.QtWidgets import (QApplication, QFileDialog, QGridLayout,
QGroupBox, QVBoxLayout, QDialog, QHBoxLayout, QLabel, QPushButton)
from PyQt5.QtRemoteObjects import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.sip import delete
from sys import argv, exit

from html import *

from DSC import win_DSC
from Text import window_text
from cancel import clear, verev_dir
from format_PH import Win

class Window(QDialog):
    
    def __init__(self):
        super(Window,self).__init__()
       
        self.createlayout()
        self.dirlist = None
    def createlayout(self) -> None:

        self.startW = QGroupBox()
        layout = QGridLayout()

        self.main_text = QLabel(self)
        self.main_text.setText("Для начала надо выбрать программу!")
        self.main_text.setFixedSize(400, 50)
        font = QFont('Serif', 15, QFont.Light)
        self.main_text.setFont(font)
        self.main_text.setAlignment(Qt.AlignCenter)

        self.ph_time = QPushButton(self)
        self.ph_time.setText("Программа разделения по времени")
        self.ph_time.clicked.connect(self.win_time)

        self.ph_DSC = QPushButton(self)
        self.ph_DSC.setText("Пограмма разделения по формату")
        self.ph_DSC.clicked.connect(self.win_dsc)

        self.ph_text = QPushButton(self)
        self.ph_text.setText("Программа разделения по выбранным цыфрам")
        self.ph_text.clicked.connect(self.text_prom)

        self.form_photo_button = QPushButton(self)
        self.form_photo_button.setText("Пограмма меняющая размер фото")
        self.form_photo_button.clicked.connect(self.form_photo)

        layout.addWidget(self.main_text)
        layout.addWidget(self.ph_time)
        layout.addWidget(self.ph_DSC)
        layout.addWidget(self.ph_text)
        layout.addWidget(self.form_photo_button)

        self.startW.setLayout(layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.startW)
        self.setLayout(main_layout)

        self.setWindowTitle("Обработчик фото")
        self.setGeometry(300,250,500,400)
        
        self.show()

        self.item = [self.main_text, self.ph_time, self.ph_DSC, self.ph_text, self.form_photo_button]

    def win_time(self):
        
        for item in self.item:
            item.deleteLater()
            del(item)

        layouton = self.layout()
        delete(layouton)

        font_title = QFont('Serif', 15, QFont.Light)

        title = QLabel(self)
        title.setText("Добро пожаловать в программу:\nРазделения фотографии по времени")
        title.adjustSize()
        title.setFont(font_title)
        title.setAlignment(Qt.AlignHCenter)

        browse = QPushButton(self)
        browse.setText("Выбрать корневую папку:")
        browse.clicked.connect(self.thread_browse)
        self.browse = browse
        
        self.browse_edit_text = QLabel(self)
        self.browse_edit_text.setFont(QFont('Arial', 11))
        self.browse_edit_text.setFixedSize(250,20)

        timecorrect = QLabel(self)
        timecorrect.setText("""<p style="text-align: center; font-size: 20px; font-weight: bold; font-family: 
Arial, sans-serif;">Что делает эта программа:</p> 
<p style="text-align: justify;font-size: 15px; line-height: 1.5; font-family: Georgia, serif;">
1.Для начала она прочитает вашу папку с фотографиями.<br>
2.Программа создаст необходимое количество папок.<br>
3.Распределит фотографии по ним.</p>
<p style="text-align: center;font-size: 15px;font-family: Georgia, serif;">
~~Вы получаете удобное распределение ваших фото по папкам~~</p>""")
        timecorrect.setAlignment(Qt.AlignTop)

        time_min = QLabel(self)
        time_min.setText("""<p style="text-align: center;font-size: 15px;font-family: Georgia, serif;">
(временной промежуток 20 минут)</p>""")

        confrim = QPushButton(self)
        confrim.setText("Подтвердить")
        confrim.clicked.connect(self.confrim_def)
        self.confrim = confrim

        cancel = QPushButton(self)
        cancel.setText("Назад")
        cancel.clicked.connect(self.cancel_def)
        self.cancel = cancel

        layout_browse = QHBoxLayout()
        layout_browse.addWidget(browse)
        layout_browse.addWidget(self.browse_edit_text)
        
        cancel_layout = QGridLayout()
        cancel_layout.addWidget(cancel, 0,9)
        cancel_layout.addWidget(confrim, 0,10)

        V_layout = QGridLayout()
        V_layout.addWidget(title, 0,0)
        V_layout.addWidget(timecorrect,1,0)
        V_layout.addWidget(time_min,2,0)
        V_layout.addLayout(layout_browse,3,0,alignment=Qt.AlignTop)
        V_layout.addLayout(cancel_layout,4,0)

        self.setLayout(V_layout)

        self.show()

        self.widget_list2 = [self.browse_edit_text,self.cancel,self.confrim,self.browse]

    def thread_browse(self):
        self.setEnabled(False)
        self.dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку","C:/Users/User/Desktop")
        x = verev_dir.iz(self,main_Window=self, dirlist=self.dirlist)
        if x == 2:
            self.dirlist = None
        self.setEnabled(True)
            
    def confrim_def(self):
        if not self.dirlist:
            dialog = notsee()
            dialog.exec_()
        else:
            from TimePh import hand
            hand(self,main_window=self,dirlist=self.dirlist, widget_list=self.widget_list2)

    def cancel_def(self):
        clear(self=self, x = 1,widget_list2=self.widget_list2)
        self.createlayout()

    def back(self,x=0):
        if x ==0:
            list_w = [self.cancel, self.confrim]      
        elif x ==1:
            list_w = [self.browse, self.browse_edit_text,self.cancel, self.confrim]
        clear(self=self, x=1, widget_list2=list_w)
        self.createlayout()

    def text_prom(self):
        for item in self.item:
            item.deleteLater()
            del(item)

        layouton = self.layout()
        delete(layouton)
        window_text(mainW = self)

    def prom(self):
        super().__init__()
        self.createlayout()

    def win_dsc(self):
        for item in self.item:
            item.deleteLater()
            del(item)

        layouton = self.layout()
        delete(layouton)
        win_DSC(mainW=self)
    
    def form_photo(self):
        for item in self.item:
            item.deleteLater()
            del(item)

        layouton = self.layout()
        delete(layouton)
        Win(MainW=self)


class notsee(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Не туда!")
        button = QPushButton()
        button.setText("Хорошо..")
        button.clicked.connect(self.ok)

        message = QLabel(self)
        message.setText("Для начала надо выбрать папку!")
        message.setFont(QFont('Arial', 11))

        layout = QGridLayout()
        layout.addWidget(message,0,0)
        layout.addWidget(button,1,0)

        self.setLayout(layout)

        self.show()

    def ok(self):
        self.accept()
        
if __name__ == "__main__":
    app = QApplication(argv)

    window = Window()
    exit(app.exec_())