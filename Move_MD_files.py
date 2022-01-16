#-*- coding: utf-8 -*-
import glob
import os
import shutil
for filename in glob.glob('*/*.md'):
   src_file = os.path.join(os.getcwd(), filename)
   dst = "C:/Users/chdls/Desktop/gitblog/voka.github.io/_posts/Daily_study/BOJ"
   dst_file =  os.path.join(dst,filename.split('\\')[-1])
   print(dst_file)
   shutil.copy2(src_file, dst_file)