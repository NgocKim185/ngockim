# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:14:26 2024

@author: Admin
"""

import random
x = float(input("Nhập giá trị x: "))
y = float(input("Nhập giá trị y: "))
def random_float_in_range(x, y):
    return random.uniform(x, y)
so_ngau_nhien = random_float_in_range(x, y)
print(f"Số thực ngẫu nhiên trong đoạn [{x}, {y}] là: ", so_ngau_nhien)