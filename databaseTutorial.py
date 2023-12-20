import random
import sqlite3
import string

#Create Connection
connection = sqlite3.connect('password.db')

#Create Cursor
cursor = connection.cursor()


#get all tables
# res = cursor.execute("SELECT tbl_name FROM sqlite_master")
# print(res.fetchall())





# Fetch column information using PRAGMA
# cursor.execute(f"PRAGMA table_info({table_name})")
# columns_info = cursor.fetchall()

# # Extract column names from the fetched information
# column_names = [col[1] for col in columns_info]

# print("Column names of the table:")
# print(column_names)
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
    return pw

def saveNewLogin():
    account_name = input("Account Name: ")
    user_name = input("User Name: ")
    email = input("Email: ")
    while True:
        try:
            genPw = int(input("1: Generate new password\n2: Enter your own password"))
            password = gen

        except:
            print("The input you have selected is not valid")




#Commit command
connection.commit()

#Close Connection
connection.close()

