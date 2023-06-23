from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials

from os import listdir, makedirs
from os.path import isdir, isfile, abspath, dirname,join
from sys import argv
from shutil import move
import sys

from sys import path

def text_handler_def(path_directory, URL_tabel, num_tabel, google_sheet,main_window):
    filelist = listdir(path_directory)
    # фильтр на JPG
    filelist_jpg =[]
    for i in filelist:
        if i.endswith(("JPG","jpg", "NEF", "png")):
            filelist_jpg.append(i)
    if len(filelist_jpg) >1:
        base_path = dirname(abspath(__file__))
        path_gogle = join(base_path, 'gogle', 'proram-dlya-photo-1a764dd4d4a4.json')
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(path_gogle, scope)
        client = authorize(creds)

        gsheet = client.open_by_url(URL_tabel)
        google_sheet_num =gsheet.worksheets()
        google_sheet_name = google_sheet_num[google_sheet].title
        wks = gsheet.worksheet(google_sheet_name)
        num_tabel = list(num_tabel)
        for num in num_tabel:
            if num != " ":
                number_exel = wks.col_values(num) + [' ']
                del number_exel[0]
                number_list = []
                for i in number_exel:
                    item = i.split("\n")
                    for element in item:
                        if element.isdigit():
                            number_list.append(int(element))
                        else:
                            elem = ''.join(filter(str.isnumeric, element))
                            if elem.isdigit():
                                number_list.append(int(elem))
                print(number_list)
                
                # #просматриваем все файлы в дериктории и работаем с ними, при необходимости создает дериктории
                directory = f"{path_directory}/готовые файлы"
                if not isdir(directory):
                    makedirs(directory)
                filelist_num = []
                for i in filelist_jpg:
                    elem = ''.join(filter(str.isnumeric, i))
                    if elem.isdigit():
                        filelist_num.append(int(elem))
                print(filelist_num)
                    
                for num in number_list:
                    for file in filelist_num:
                        if num == file:
                            file_1 =f"{path_directory}/{filelist_jpg[filelist_num.index(file)]}"
                            file_2 = f"{path_directory}/{directory}/{filelist_jpg[filelist_num.index(file)]}"
                            if isfile(file_1) and not isfile(file_2):
                                move(file_1, directory)
                            break
        from .Window_text import end_text
        dialog = end_text(directory=directory)
        dialog.exec()
    else:
        del(path_directory)
        path.append("..")
        from cancel import notJPG
        main_window.setEnabled(False)
        dialog = notJPG()
        dialog.exec()
        main_window.setEnabled(True)