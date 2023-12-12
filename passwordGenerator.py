import random
import string

def generate_pw(min_length, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters
    if numbers:
        characters += digits

    if special_chars:
        characters += special

    pw = ""
    meets_req = False
    contains_special = False
    contains_number = False
    if not numbers:
        contains_number = True
    if not special_chars:
        contains_special = True

    while not meets_req or len(pw)<min_length:
        new_char = random.choice(characters)
        pw += new_char
        if not contains_number and new_char in digits: 
            contains_number = True
        if not contains_special and new_char in special: 
            contains_special = True
        if contains_special and contains_number and len(pw)>=min_length:
            meets_req = True
    print(pw)

print("Main Menu\n")
print("1: Generate New Password\n\n")
boot = True
while boot:
    try:
        num = int(input("What would you like to do?:"))
        if num==1:
            generate = True
            while generate:
                try:
                    num = int(input("What is the length of the pw you would like to create?: "))
                    number = input("Would you like your password to include numbers?(y/n): ")
                    special = input("Would you like your password to include special characters?(y/n): ")
                    req_number = False
                    req_special = False
                    if number == "y":
                        req_number = True
                    if special == "y":
                        req_special = True
                    generate_pw(num, req_number, req_special)
                    generate = False
                except ValueError:
                    print("Invalid input. Please another option.")
            boot = False
    except ValueError:
        print("Invalid input. Please enter an integer.")





