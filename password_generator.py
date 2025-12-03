# ==============================================
#  Program: Password Generator
#  Author: Luboš Kulhan | alias: Adam Kaiser
#  Description: Program for generating passwords
# ==============================================

import os
import random as r

# characters for password
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbrers = ['0', '1', '2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']
special_chars = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '_', '{', '|', '}']

def clear():
    os.system('clear')

def welcome():
    while True:
        length = 0
        password = ""
        clear()
        print("Welcome to password generator!\n")

        while True:
            try:
                length = input("Set length of your password: ")
                length = int(length)
                if length < 0:
                    clear()
                    print("Input only natural numbers...\n")
                elif length == 0:
                    clear()
                    print("Password must have length...\n")
                else:
                    clear()
                    break
            except ValueError:
                clear()
                print("Input only numbers...\n")

        while True:
            try:
                print("What type of password?\n1. decimal (weak)\n2. letters (moderate)\n3. combination (strong)")
                choice = input("Choose (1,2,3): ")
                choice = int(choice)
                if choice < 1:
                    clear()
                elif choice > 3:
                    clear()
                else:
                    clear()
                    break
            except ValueError:
                clear()
        
        # Generator
        i = 1
        match choice:
            case 1:
                while i <= length:
                    char = r.choice(numbrers)
                    password = password + char
                    i += 1
                print(f"Your newly generated password: {password}")
                input("\nPress anything to continue...")
            case 2:
                ran_list = lower_case + upper_case
                while i <= length:
                    char = r.choice(ran_list)
                    password = password + char
                    i += 1
                print(f"Your newly generated password: {password}")
                input("\nPress anything to continue...")
            case 3:
                super_ran_list = lower_case + upper_case + numbrers + special_chars
                while i <= length:
                    char = r.choice(super_ran_list)
                    password = password + char
                    i += 1
                print(f"Your newly generated password: {password}")
                input("\nPress anything to continue...")

# Start of program -------------------------------------------------
welcome()