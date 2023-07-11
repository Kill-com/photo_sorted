from os import listdir,makedirs,remove
from os.path import isdir, isfile
from PIL.Image import open,new

def handler(file_path, form):
    file = listdir(file_path)
    file_jpg = []
    for i in file:
        if i.endswith(("JPG","jpg", "NEF", "png")):
            file_jpg.append(i)
    if len(file_jpg) >1:
        if form == 1:
            H = 1205
            V = 1795
            S_cube = 1205
        elif form == 2:
            H = 1795
            V = 2398
            S_cube = 1795
        elif form == 3:
            H = 2398
            V = 3602
            S_cube = 2398
        directory = f"{file_path}/Фото с измененным размером"
        if not isdir(directory):
            makedirs(directory)
        for i in file_jpg:
            photo = open(f"{file_path}/{i}")
            if photo.width == photo.height:
                end_photo = new("RGB", (H, V), "black")
                S_foto = photo.resize((S_cube,S_cube))
                end_photo.paste(S_foto, ((H - S_foto.width) // 2, (V - S_cube.height) // 2))
            else:
                if photo.height > photo.width:
                    end_photo = photo.resize((H,V))
                else:
                    end_photo = photo.resize((V,H))
            if isfile(f"{directory}/{i}"):
                remove(f"{directory}/{i}")
            end_photo.save(f"{directory}/{i}")
        return(1, directory)
        
                
    else:
        del(file_path)
        del(form)
        return(2,None)