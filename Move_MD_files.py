#-*- coding: utf-8 -*-
import glob
import os
import shutil
for filename in glob.glob('*/*.md'):
   src_file = os.path.join(os.getcwd(), filename)
   dst = ""
   dst_file =  os.path.join(dst,filename.split('\\')[-1])
   print(dst_file)
   shutil.copy2(src_file, dst_file)