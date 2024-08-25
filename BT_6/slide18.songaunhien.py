# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:12:19 2024

@author: Admin
"""

import random
start = int(input("Giá trị start: "))
stop = int(input("Giá trị stop: "))
step = int(input("Giá trị step: "))
def random_number_from_range(start, stop, step):
    return random.randrange(start, stop, step)
so_ngau_nhien = random_number_from_range(start, stop, step)
print(f"Số ngẫu nhiên từ dãy ({start}, {stop}, {step}) là: ", so_ngau_nhien)