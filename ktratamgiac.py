# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:40:50 2024

@author: Student
"""

print("Tìm loại tam giác")
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a+b>c and a+c>b and b+c>a:
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("Tam giác vuông.")
    elif a == b or a ==c or b ==c:
        print("Tam giác cân.")   
    elif a == b and b == c:
        print("Tam giác đều.")
    elif a*a>b*b+c*c or b*b>a*a+c*c or c*c>a*a+b*b:   
        print("Tam giác tù.")
else:
    print("Tam giác thường.")    