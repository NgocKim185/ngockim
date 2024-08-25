# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 13:41:50 2024

@author: Student
"""

N = int(input("Nhập số nguyên dương có 2 chữ số: "))
if 10<=N<=99:
    Hang_chuc = N//10
    Hang_don_vi = N % 10
    Tong = Hang_chuc + Hang_don_vi
    print("Tổng các chữ số của N là: " ,Tong)
else:
    print("Nhập số nguyên dương có 2 chữ số!")    