import string
import random

# Handles Collection of data from user
def collect_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    return first_name,last_name,email

#Generates a Password of length Nine(9)
def password_gen(first,last):
    letters = string.ascii_letters
    randstr = ""
    diff = 9 - (len(first[0:2])+len(last[-2:]))
    for i in range(diff):
        randstr += random.choice(letters)
    passkey = first[0:2] +(last[-2:]) + randstr
    del i
    return passkey

#Outputs collected user details
def display_details(first_name,last_name,email):
    str3 = "-"
    str3 = str3.center(30,'-')
    print(f'''\nUser Details Collected
{str3}
Name: {first_name} {last_name}
Email: {email}
    ''')

# Builds a high level data structure for storing user details 
# by implementing a list of Dictionaries
def database_build(first_name,last_name,email,password):
    user_details = {
        "First name": first_name,
        "Last name": last_name,
        "Email": email,
        "Password": password
    }
    db.append(user_details)
    return db

# Outputs data stored in the Database
def display_db(database):
    str2 = '-'
    str2 = str2.center(30,'-')
    print(f'''\nUser Data is in the database
{str2}''')
    for user in db:
        Name1= user["First name"]
        Name2= user["Last name"]
        Mail = user["Email"]
        Password = user['Password']
        print(f'''Name:{Name1} {Name2}
Email:{Mail}
Password:{Password}
''')

db = []
count = 1
answer = "no"
while answer == "no":                      
    # While there is another user
    str = "Welcome, Please enter your First name, Last name and an Email address"
    str = str.center(140)
    print(str)

    first_name,last_name,email = collect_data()
    passkey = password_gen(first_name,last_name)

    print("Suggested password = ",passkey)
    response =input("Are you satisfied with the suggested password? [y/n] > ").lower()

    if response == "y":
        display_details(first_name,last_name,email)
        database_build(first_name,last_name,email,passkey)                         
        last_user =input("Are you the last user [y/n] > ").lower()
        if last_user == "y":
            answer = "yes"
        else:
            count+=1
            
    else:
        password = input("Create a password: ")
        while len(password) <7:
            password = input("Enter password greater than 6 characters: ")
        else:
            print("\nPassword set to:",password)
            display_details(first_name,last_name,email)
            #Appending the data to database
            database_build(first_name,last_name,email,password)      
            last_user =input("Is this the last user [y/n] > ").lower()
            if last_user == "y":
                answer= "yes"
            else:
                count+=1
                

display_db(db)