import random
import string
import sqlite3

connection = sqlite3.connect('password.db')

cursor = connection.cursor()


table_name = 'logins'

def displayLogins():
    cursor.execute("SELECT * FROM logins")
    logins = cursor.fetchall()
    if len(logins)==0:
        print("There are no saved logins!")
    else:
        print("Account Name\t|\tUsername\t|\tPassword\t|\tEmail")
        print("-----------------------------------------------------------------------------------")
        for login in logins:
            row = ""
            i=0
            for item in login:
                i=i+1
                if i==1:
                    row="\t   "+item
                else:
                    row+="\t\t"+item
            print(row+"\n")

def getLoginDetails():
    column_name = 'website_name'
    account = input("Enter the account name of the login details you would like to see: ").lower()
    query = f"SELECT * FROM {table_name} WHERE {column_name} = ?"
    cursor.execute(query, (account,))
    res = cursor.fetchone()
    if res==None:
            print("That account does not exist!")
    else:
        print("Account Name\t|\tUsername\t|\tPassword\t|\tEmail")
        print("-----------------------------------------------------------------------------------")
        row=""
        for item in res:
            row+="\t\t"+item
        print(row)
    
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
    account_name = input("Account Name: ").lower()
    user_name = input("User Name: ")
    email = input("Email: ")
    password=""
    while True:
        try:
            genPw = int(input("1: Generate new password\n2: Enter your own password"))
            if genPw==1:
                length = int(input("How long do you want your passowrd to be? "))
                numbers = input("Would you like your password to include numbers? (y/n)")
                special = input("Would you like your password to include special characters? (y/n)")
                password=generate_pw(length, numbers=="y", special=="y")
                break
            if genPw==2:
                password = input("Please enter your password: ")
                break
            else:
                print("Invalid selection")
        except:
            print("The input you have selected is not valid")
    new_record_data = (account_name, user_name, password, email)  # Replace with actual values

    insert_query = f"INSERT INTO {table_name} (website_name, user_name, password, email) VALUES (?, ?, ?,?)"
    cursor.execute(insert_query, new_record_data)
    connection.commit()
    print("New Login Saved!\n")

def main():    
    boot = True
    while boot:
        print("Main Menu\n")
        print("1: View All Logins\n")
        print("2: Get Login Details\n")
        print("3: Save A New Login\n")
        print("4: Delete A Login\n")
        print("5: Exit\n")
        try:
            num = int(input("What would you like to do?: "))
            if num==1:
                displayLogins()
            if num==2:
                getLoginDetails()
            if num==3:
                saveNewLogin()
            if num==4:
                print("fadsfa")
            if num==5:
                boot = False
                break
            goBack = input("Back to Main menu? (y/n)")
            if goBack.lower()=="n":
                boot=False
        except ValueError:
            print("\nInvalid input. Please try again\n")

main()



#Commit command
connection.commit()

#Close Connection
connection.close()

