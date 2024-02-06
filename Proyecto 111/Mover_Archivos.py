import os
import shutil

from_dir = "C:\\Users\\danny\\OneDrive\\Descargas"
to_dir = 'C:\\Users\\danny\\OneDrive\\Documentos\\programacion\\Documentos_Archivos'

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
       
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Documentos_Archivos"
        path3 = to_dir + '/' + "Documentos_Archivos" + '/' + file_name

     
        if os.path.exists(path2):
            print("Moviendo " + file_name + ".....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moviendo " + file_name + ".....")
            shutil.move(path1, path3)
