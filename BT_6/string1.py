# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:50:51 2024

@author: Student
"""

text='Đại học Quốc gia, Khu phố 6, P. Linh Trung, T. Thủ Đức, Tp. HCM'
text=text.replace("P. ","").replace("T. ","").replace("Tp. ","")
sub_string=text.split(", ")
for sub in sub_string:
    print (sub)