# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:04:35 2024

@author: Student
"""
GPA = float(input("Nhập điểm trung bình (GPA):"))
if GPA < 3.5:
        print("Học lực Kém")
if GPA >= 3.5 and GPA < 5.0:
        print("Học lực Yếu")
if GPA >= 5.0 and GPA < 7.0:
        print("Học lực Trung Bình")
if GPA >= 7.0 and GPA < 8.0:
        print("Học lực Khá")
if GPA >= 8.0 and GPA < 9.0:
        print("Học lực Giỏi")
if GPA >= 9.0 and GPA <= 10:
        print("Học lực Xuất Sắc")        
        
        