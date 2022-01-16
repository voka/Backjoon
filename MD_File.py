#-*- coding: utf-8 -*-
import os

class md_file():
    def __init__(self,Dates,fname,problem_no,Gist_Script):
        self.new_Folder_Path = os.path.join('./md_files',Dates)
        self.fname = fname
        self.new_md_file = os.path.join(self.new_Folder_Path,fname)
        with open("./Sample.md", "r", encoding="UTF-8") as file_obj:
            self.file_content = file_obj.readlines()
        self.websites = "[문제링크](https://www.acmicpc.net/problem/{0})".format(problem_no)
        self.Gist_Script = Gist_Script
    
    def createFolder(self):
        try:
            if not os.path.exists(self.new_Folder_Path):
                os.makedirs(self.new_Folder_Path)
        except OSError:
            print ('Error: Creating directory. ' +  self.new_Folder_Path)
    def Modify_Contents(self):
        self.file_content[1] = 'title: "{0}"\n'.format(self.fname.split('.')[0])
        self.file_content.append("\n\n")
        self.file_content.append(self.websites)
        self.file_content.append("\n\n\n")
        self.file_content.append(self.Gist_Script)
    def Write_md_file(self):
        f = open(self.new_md_file,'w',encoding="UTF-8")
        f.writelines(self.file_content)
        f.close()


"""
--- Test ---
Dates = '20220116'
fname = '백준 10164 격자상의 경로.md'
problem_no = 14002
Gist_Script = '<script src="https://gist.github.com/voka/77951def35de63b887eb5f4cd43c9602.js"></script>'
md = md_file(Dates,fname,problem_no,Gist_Script)
md.createFolder()
md.Modify_Contents()
md.Write_md_file()
"""