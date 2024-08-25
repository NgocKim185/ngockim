# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:39:37 2024

@author: Student
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
tong = a+b
hieu = a-b
tich = a*b
thuong = a/b
chia_lay_du = a%b
chia_lay_nguyen = a//b
print("Tổng là: ", tong)
print("Hiệu là: ", hieu)
print("Tích là: ", tich)
print("Chia lấy dư là: ", chia_lay_du)
print("Chia lấy nguyên là: ", chia_lay_nguyen)
#Làm tròn 2 số sau khi chia
number = thuong
rounded_2 = round(number, 2)
print("Thương sau khi làm tròn 2 chữ số: ", rounded_2)
#Làm tròn 3 số sau khi chia
number = thuong
rounded_3 = round(number, 3)
print("Thương sau khi làm tròn 3 chữ số: ", rounded_3)