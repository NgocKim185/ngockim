# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:23:29 2024

@author: Admin
"""
import math
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
ab=a*b
can_a=math.sqrt(a)
can_b=math.sqrt(b)
can4_a=math.pow(a,1/4)
can4_b=math.pow(b,1/4)
can4_ab=math.pow(ab,1/4)
x1=(can_a - can_b) / (can4_a - can4_b)
x2=(can_a + can4_ab) / (can4_a + can4_b)
ket_qua= x1 - x2
print("Kết quả là: ", ket_qua)
number=ket_qua
print("Kết quả sau làm tròn: ", round(ket_qua, 3))

