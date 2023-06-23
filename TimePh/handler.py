from os import listdir, makedirs, rename
from os.path import getmtime, join, isdir
from shutil import move

from sys import path

from .window_end import not_photo, window_end_W

path.append("..")
from cancel import notJPG

def hand(self,main_window, dirlist, widget_list):
    filelist = listdir(dirlist)
    # фильтр на JPG
    filelist_jpg =[]
    for i in filelist:
        if i.endswith(("JPG","jpg", "NEF", "png")):
            filelist_jpg.append(i)
    if len(filelist_jpg) >1:
        # сортируем по файлы по времени
        filelist_jpg = sorted(filelist_jpg, key=lambda x: getmtime(join(dirlist, x)))
        # делаем список времени
        timelist =[]
        for file in filelist_jpg:
            time = getmtime(join(dirlist,file))
            timelist.append(time)
        # делаем временный список файлов первой фотоссесии
        a =0
        many =1
        con = 1
        for time in timelist:
            if timelist.index(time)+1 <len(timelist):
                if timelist[timelist.index(time)+1]-time >1200:
                    break
            else:
                if time - timelist[timelist.index(time)-1]>1200:
                    break
                else:
                    del(dirlist)
                    see = not_photo(self, widget_list)
                    see.exec()
                    con +=1
        if con ==1:
            for time in timelist:
                if timelist.index(time)+1<len(timelist):
                    if timelist[timelist.index(time)+1]-time >1200:
                        a +=1
                        derictory = f"{dirlist}/Фотосессия №{a}"
                        if not isdir(derictory):
                            makedirs(derictory)
                        while many !=-1:
                            many -=1
                            if many ==-1:
                                pass
                            else:
                                move(f"{dirlist}/{filelist_jpg[timelist.index(time)-many]}",derictory)
                        many = 1
                    else:
                        many +=1
                else:
                    if time - timelist[timelist.index(time)-1] >1200:
                        a+=1
                        derictory = f"{dirlist}/Фотосессия №{a}"
                        if not isdir(derictory):
                            makedirs(derictory)
                        while many !=-1:
                            many -=1
                            if many ==-1:
                                pass
                            else:
                                move(f"{dirlist}/{filelist_jpg[timelist.index(time)-many]}",derictory)
                        many = 1
                    else:
                        if many > 1:
                            a +=1
                            derictory = f"{dirlist}/Фотосессия №{a}"
                            if not isdir(derictory):
                                makedirs(derictory)
                            while many !=-1:
                                many -=1
                                if many ==-1:
                                    pass
                                else:
                                    move(f"{dirlist}/{filelist_jpg[timelist.index(time)-many]}",derictory)
                        else:
                            derictory = f"{dirlist}/Фотосессия №{a}"
                            if not isdir(derictory):
                                del(dirlist)
                                main_window.setEnabled(False)
                                see = not_photo(self, widget_list)
                                see.exec()
                            else:
                                move(f"{dirlist}/{filelist_jpg[timelist.index(time)]}",derictory)
                                many = 1
            window_end_W(main_window=self, widget_list=widget_list)
    else:
        del(dirlist)
        main_window.setEnabled(False)
        dialog = notJPG()
        dialog.exec()
        main_window.setEnabled(True)
    

