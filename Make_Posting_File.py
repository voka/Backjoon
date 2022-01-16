#-*- coding: utf-8 -*-
import os
import Gist
import MD_File
Dates = input() # 날짜 -> 폴더명 입력 
Year,Month,Day = Dates[:4],Dates[4:6],Dates[6:8]
#print(Year,Month,Day)
folder_path = os.path.join(os.getcwd(),Dates)
#print(folder_path)
file_names = os.listdir(folder_path)
problem_nos = {fname:fname.split()[1] for fname in file_names}
#print(problem_nos)
md_file_names ={fname:Year+'-'+Month+'-'+Day+'-'+fname.split('.')[0]+'.md' for fname in file_names}
file_paths = [os.path.join(folder_path,fname) for fname in file_names]
#print(file_paths,md_file_names)


# Gist class
MyGist = Gist.Gist()
#Gist 파일 만들어야 할 경우
MyGist.filepath_list = file_paths
MyGist.Create()
#
MyGist.file_names = file_names
MyGist.make_Scripts_Str()


# Md class
for fname in file_names:
    md = MD_File.md_file(Dates,md_file_names[fname],problem_nos[fname],MyGist.Gist_scripts[fname])
    md.createFolder()
    md.Modify_Contents()
    md.Write_md_file()