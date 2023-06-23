from os import listdir, path, makedirs
from os.path import isdir
from shutil import move

from re import sub

def DSC_handler_def(path_start_directory, path_DSC_directory, you_directory = None):
    directory = f"{path_start_directory}/выбор_DSC"
    if you_directory is not None or you_directory !=" ":
        if isdir(f"{path_start_directory}/{you_directory}"):
            if listdir(f"{path_start_directory}/{you_directory}") is None:
                directory = f"{path_start_directory}/{you_directory}"
            else:
                del path_start_directory, path_DSC_directory, you_directory
                return(3,None)
    full_file_list = listdir(path_start_directory)
    jpg_file_list =[]
    jpg_file_list_int = []
    for i in full_file_list:
        if i.endswith(("JPG","jpg", "NEF", "png")):
            digits = sub(r'\D', '', i)
            if digits.isdigit():
                jpg_file_list.append(i)
                jpg_file_list_int.append(int(digits))
                
    if len(jpg_file_list) >1:     
        DSC_file_list = listdir(path_DSC_directory)
        DSC_file_list_jpg = []
        for i in DSC_file_list:
            if i.endswith(("JPG","jpg", "NEF")):
                digits = sub(r'\D', '', i)  # удаление нецифровых символов
                if digits.isdigit():
                    DSC_file_list_jpg.append(int(digits))
        if not isdir(directory):
            makedirs(directory)
        for i in DSC_file_list_jpg:
            for item in jpg_file_list_int:
                if i == item:
                    try:
                        move(f"{path_start_directory}/{jpg_file_list[jpg_file_list_int.index(i)]}", directory)
                        break
                    except:
                        return(3, None)
        return(1, directory)
    else:
        del(path_start_directory)
        return(2,None)