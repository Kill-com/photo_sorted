from PyQt5.sip import delete
from PyQt5.QtWidgets import QLabel, QDialog, QPushButton, QVBoxLayout
from os import listdir

def clear(self,x = 1,widget_list2 = None):
    if x == 1:
        layouton = self.layout()
        widget_list = []
        for i in range(layouton.rowCount()):
            for j in range(layouton.columnCount()):
                item = layouton.itemAtPosition(i, j)
                if item is not None:
                    widget = item.widget()
                    if widget is not None:
                        widget_list.append(widget) # Непосредственно виджет добавляем в список

        for widget in widget_list:
            widget.deleteLater() # Вызываем метод deleteLater для виджета
        delete(layouton)

    if not widget_list2:
        pass
    else:
        for widget in widget_list2:
            widget.deleteLater()
class verev_dir(QDialog):
    def __init__(self):
        super(verev_dir,self).__init__()
        
    def iz(self,main_Window, dirlist, x = 0):
        a = 0
        if not dirlist:
            pass
        else:
            for i in listdir(dirlist):
                if i.endswith(("JPG", "jpg", "NEF", "png")):
                    if x == 0:
                        main_Window.browse_edit_text.setText(dirlist)
                    else:
                        return(1)
                    a +=1
                    break
            
            if a == 0:
                dirlist = None
                dialog = notJPG()
                dialog.exec()
                return(2)
class notJPG(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Нету JPG...")
        button = QPushButton()
        button.setText("Хорошо..")
        button.clicked.connect(self.ok)

        message = QLabel()
        message.setText("В папке не было найдено файлов\nс расшерением JPG или он вего один")

        layout = QVBoxLayout()
        layout.addWidget(message)
        layout.addWidget(button)

        self.setLayout(layout)
        self.show()

    def ok(self):
        self.accept()

