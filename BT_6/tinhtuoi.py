# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 14:07:35 2024

@author: Student
"""

namsinh = int(input("Nhập năm sinh: "))
namhientai = 2024
if 0< namsinh <=2024:
    tuoi= namhientai - namsinh
    print("Tuổi của bạn là: ", tuoi)
else:
    print("Năm sinh không hợp lệ")    