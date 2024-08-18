# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:53:08 2024

@author: Student
"""

km = float(input("Số km mà bạn đã đi là: "))
if km <= 1 :
    x=km*20
elif km <= 3:
    x=km*13
elif km <= 8:
    x=13*3 + (km-3)*12
else:
    x=13*3 + 12*5 + (km-8)*10
if x>100:
    x=x*0.92
print(f"Số tiền phải trả là: {x}k ")    