# db = "db.csv"
# def signup(filename):
#     with open(filename, "r") as file:
#         lines = file.readlines()
#         headers = lines[0].split('|')
#         records = [line.split('|') for line in lines[1:]]

#     usernames = [record[0] for record in records]

#     username_exists = True
#     while username_exists:
#         username = input("Enter username: ")
#         if len(username) == 0:
#             print("Username can't be empty")
#         if username in usernames:
#             print("Username already taken, try something else")
#         else:
#             username_exists = False

#     password = input("Enter password: ")
#     name = input("Enter full name: ")
#     dob = input("Enter dob: ")
#     class_ = input("Enter class: ")
#     section = input("Enter section: ")
#     phone_number = input("Enter phone number: ")
#     gender = input("Enter gender: ")
#     address = input("Enter address: ")

#     record = '|'.join([username, password, name, dob, class_, section, phone_number, gender, address, '\n'])
#     with open(filename, 'a') as file:
#         file.write(record)

#     print("Signup successful")


# def login(filename):
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ").strip()

#     with open(filename, "r") as file:
#         lines = file.readlines()
#         records = [line.split('|') for line in lines[1:]]


#     for record in records:
#         if record[0] == username and record[1] == password:
#             print("Login Successful")
#             return True
#     print("Incorrect Username/Password")
#     return False


# def check_record(filename, value, column="name"):
#     with open(filename, "r") as file:
#         lines = file.readlines()
#         header = lines[0].split('|')
#         records = [line.split('|') for line in lines[1:]]
#     if column not in header:
#         print("Invalid column")
#     index = header.index(column)
#     matching_records = []
#     for record in records:
#         if record[index] == value:
#             matching_records.append(record)

#     if len(matching_records) == 0:
#         print("No record exists where {} = {}".format(column, value))
#     else:
#         # print('|'.join(header[:-1]))
#         for i in matching_records:
#             print('|'.join(i))
#         return matching_records

# # signup(db)
# login(db)

# check_record(db, "bhav", column="username")





# import os
# from datetime import datetime
# # print(datetime.now())
# def quiz_upl():
#     db = "Computer Science Quiz\\" + "Quiz" + str(len(os.listdir("Computer Science Quiz")) + 1) + f"_{str(datetime.now())[:10]}" + ".csv"
#     # print(db)
#     # Question| Option A| Option B| Option C| Option D| Answer
#     def quiz(filename=str(db)):
#         try:
#             with open(filename, "r") as file:
#                 pass
#         except:
#             with open(filename, "w") as file:
#                 file.write("Question| Option A| Option B| Option C| Option D| Answer\n")
#         with open(filename, "r") as file:
#             lines = file.readlines()
#             # print(lines[0])
#             headers = lines[0].split('|')
#             records = [line.split('|') for line in lines[1:]]

#         questions = [record[0] for record in records]
#         ans = "yes"
#         while ans == "yes":
#             question_exists = True
#             while question_exists:
#                 question = input("Enter question: ")
#                 if len(question) == 0:
#                     print("question can't be empty")
#                 if question in questions:
#                     print("Question is already present")
#                 else:
#                     question_exists = False

#             OA = input("Enter option A: ")
#             OB = input("Enter option B: ")
#             OC = input("Enter option C: ")
#             OD = input("Enter option D: ")
#             Answer = input("Enter answer(A,B,C or D): ").upper()
#             ans = input("do you wanna continue?(yes or no): ").lower()
        

#             record = '|'.join([question, OA, OB, OC, OD, Answer, '\n'])
#             with open(filename, 'a') as file:
#                 file.write(record)

#         print("success")

#     quiz(db)

# quiz_upl()





from tkinter import *
