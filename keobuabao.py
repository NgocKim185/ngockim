# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:47:29 2024

@author: Student
"""

import random
def get_computer_choice():
    return random.choice(['kéo', 'búa', 'bao'])
def get_user_choice():
    choice = input("Mời bạn chọn kéo, búa hoặc bao: ").lower()
    while choice not in ['kéo', 'búa', 'bao']:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
        choice = input("Mời bạn chọn kéo, búa hoặc bao: ").lower()
    return choice
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Hòa"
    elif (user_choice == 'kéo' and computer_choice == 'bao') or \
         (user_choice == 'búa' and computer_choice == 'kéo') or \
         (user_choice == 'bao' and computer_choice == 'búa'):
        return "Người thắng"
    else:
        return "Máy thắng"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Người ra: {user_choice}")
    print(f"Máy ra: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(f"Kết quả: {result}")
play_game()    