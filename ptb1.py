# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:33:56 2024

@author: Student
"""

a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
#thực hiện phép tính
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là:", x)
      