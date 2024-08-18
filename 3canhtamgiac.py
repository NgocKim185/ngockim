# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:26:58 2024

@author: Student
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
#Kiểm tra
if a==0 or b==0 or c==0:
    print("Cạnh của tam giác không thể bằng 0")
if a+b>c and a+c>b and b+c>a:
    print("a,b,c là 3 cạnh của 1 tam giác")
else:
    print("a,b,c không phải là 3 cạnh của 1 tam giác")    