from tkinter import *
import os
from datetime import datetime
import shutil
from tkinter import filedialog
import csv
# from xml.sax import default_parser_list
##scired
# username Password Name Class-Section DOB Address

# ask for topics
# differentiate based on difficulty - Problematic
'''
intro
modules
functions(use) and variables and their data types
code
output
bib

'''
#https://www.youtube.com/watch?v=H71ts4XxWYU
#https://www.tutorialspoint.com/How-to-copy-files-from-one-folder-to-another-using-Python
#
#completed???


# Unique folder name according to <Teacher Name><Subject Name>...

"""
list of folder ke button bana de using eval
button click -> toplevel with quiz names as buttons -> click button -> def attempt quiz  
"""




"""
password, name, dob, class_, section, phone_number, gender, address
"""

db = "db.csv"
def signup(username, password, name, dob, class_, section, phone_number, gender, address, filename="db.csv"):
    with open(filename, "r") as file:
        lines = file.readlines()
        headers = lines[0].split('|')
        records = [line.split('|') for line in lines[1:]]

    usernames = [record[0] for record in records]

    username_exists = True
    while username_exists:
        # username = input("Enter username: ")
        if len(username) == 0:
            return "Username can't be empty"
        if username in usernames:
            return "Username already taken, try something else"
        else:
            username_exists = False

    # password = input("Enter password: ")
    # name = input("Enter full name: ")
    # dob = input("Enter dob: ")
    # class_ = input("Enter class: ")
    # section = input("Enter section: ")
    # phone_number = input("Enter phone number: ")
    # gender = input("Enter gender: ")
    # address = input("Enter address: ")

    record = '|'.join([username, password, name, dob, class_, section, phone_number, gender, address, '\n'])
    with open(filename, 'a') as file:
        file.write(record)

    return "Signup successful"


def login(username, password, filename = "db.csv"):
    # username = username.strip()
    # password = password.strip()

    with open(filename, "r") as file:
        lines = file.readlines()
        records = [line.split('|') for line in lines[1:]]


    for record in records:
        if record[0] == username and record[1] == password:
            print(username)
            stu.destroy()
            profile(username)
            return "Login Successful"
            # return True
    return "Incorrect Username/Password"



def check_record(value, column="username", filename = "db.csv"):
    with open(filename, "r") as file:
        lines = file.readlines()
        header = lines[0].split('|')
        records = [line.split('|') for line in lines[1:]]
    if column not in header:
        print("Invalid column")
    index = header.index(column)
    matching_records = []
    for record in records:
        if record[index] == value:
            matching_records = record
            break

    if len(matching_records) == 0:
        print("No record exists where {} = {}".format(column, value))
    else:
        # print('|'.join(header[:-1]))
        # for i in matching_records:
            # print('|'.join(i))
        return matching_records
























count = 0
def profile(u_name):
    #extract things form database
    prof = Toplevel(root)
    prof.title("Profile")
    prof.geometry("1000x500+450+300")
    prof.iconphoto(False, icon)
    pers_details = Frame(prof, bg='black', height = 1200, width=480)
    pers_details.grid(row=0, column=0)
    # pic = Frame(pers_details, bg='white', height = 250, width=500)
    # pic.pack()
    lst = check_record(u_name)
    print(lst)
    # with open("Credentials.txt") as file:
    #     lst_temp = file.readline().split("    ")
    #     if lst_temp[0] == u_name:
    #         lst = lst_temp


    #username, password, name, dob, class_, section, phone_number, gender, address
    
    spaces_above = Label(pers_details, text = "\n\n\n\n\n\n", bg = 'black', fg = 'black')
    spaces_above.pack()

    name = Label(pers_details, text = f"Name: {lst[2]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    name.pack()

    dob = Label(pers_details, text = f"DOB: {lst[3]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    dob.pack()

    class_sec = Label(pers_details, text = f"Class-Section: {lst[4]}-{lst[5]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    class_sec.pack()

    gender = Label(pers_details, text = f"Gender: {lst[7]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    gender.pack()

    mobile = Label(pers_details, text = f"Mobile Number: +91 {lst[6]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    mobile.pack()

    address = Label(pers_details, text = f"Address: {lst[8]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    address.pack()

    spaces_below = Label(pers_details, text = "\n"*25, bg = 'black', fg = 'black')
    spaces_below.pack()

    assign = Frame(prof, height = 1080)
    assign.grid(row = 0, column=1)

    # main_cont = Frame(assign)
    # main_cont.pack()

    dropdwn = Frame(assign, padx=800)
    dropdwn.pack()

    options = ['Assignments', 'Quizes']
    result = StringVar()
    result.set("--None--")
    drop = OptionMenu(dropdwn, result, *options)
    drop.grid(row=0, column=0)

    drop_result = Frame(assign)
    drop_result.pack()

    default_result = Label(drop_result, text="Nothing to show.\nPlease select a choice", padx=650, font=("Courier", 15))
    default_result.pack()

    lst_subjects = []
    """for i in os.listdir("E:\CS Investigatory Project__"):
        if os.path.isdir(i):
            print(True)"""
    












    def assigns():
        if result.get() == "--None--":
            pass
        else:
            # print(result.get())
            default_result.config(text = f"{result.get()}")
            if result.get() == "Assignments":
                fold = Toplevel(root)
                fold.geometry("1000x500+200+500")
                topic = Label(fold, text = "Details", font = ('Courier', 10))
                topic.pack()
                def open_folder():
                    lst_dir = os.listdir("./")
                    for i in lst_dir:
                        if f"{name_teach.get()}_{sub_teach.get()} Assignment".lower() == i.lower():
                            fileopen = filedialog.askopenfilename(initialdir=i)
                            os.startfile(fileopen)
                            fold.destroy()
                            break
                    else:
                        warninglbl = Label(fold, text = "Folder not found!", font = ('Courier', 10), fg='red')
                        warninglbl.pack()

                name_teach = Entry(fold)
                sub_teach = Entry(fold)
                name_teach.insert(0, "---Enter teacher name here---")
                sub_teach.insert(0, "---Enter Subject---")
                name_teach.pack()
                sub_teach.pack()
                fold_open = Button(fold, text = "Open Assignment folder", command = open_folder)
                fold_open.pack()
            
            elif result.get() == "Quizes":
                fold = Toplevel(root)
                fold.geometry("1000x500+200+500")
                topic = Label(fold, text = "Details", font = ('Courier', 10))
                topic.pack()
                def open_folder():
                    lst_dir = os.listdir("./")
                    for i in lst_dir:
                        if f"{name_teach.get()}_{sub_teach.get()} Quiz".lower() == i.lower():
                            fileopen = filedialog.askopenfilename(initialdir=i)
                            fold.destroy()
                            quiz_stu = Toplevel(prof)
                            quiz_stu.geometry("1000x500+450+300")

                            title_uq = Label(quiz_stu, text = "Quiz", height=5, font=("Courier", 15), bg = "orange", width="50")
                            title_uq.pack()

                            ques = Label(quiz_stu, text = "", height=5, font=("Courier", 15),bg = "cyan")
                            ques.pack()

                            oa = Label(quiz_stu, text = "", height=5, font=("Courier", 15),bg = "yellow")
                            oa.pack()
                            ob = Label(quiz_stu, text = "", height=5, font=("Courier", 15),bg = "blue")
                            ob.pack()
                            oc = Label(quiz_stu, text = "", height=5, font=("Courier", 15),bg = "red")
                            oc.pack()
                            od = Label(quiz_stu, text = "", height=5, font=("Courier", 15), bg = "Green")
                            od.pack()
                            

                            final_ans = Entry(quiz_stu)
                            final_ans.insert(0, "Enter Answer(A,B,C or D)")
                            final_ans.pack()

                            global count
                            count = 1
                            def update():
                                warning_quiz.config(text = "")
                                global count
                                final_ans.delete(0, END)
                                final_ans.insert(0, "Enter Answer(A,B,C or D)")
                                cont.pack_forget()
                                count_ = count
                                # count_ = readlst.index(j)
                                count_ +=1
                                # print(count_)
                                if count_ < len(readlst):
                                    j = readlst[count_]
                                    ques.config(text = "Question:" + j[0])
                                    oa.config(text = "A)"+j[1])
                                    ob.config(text = "B)"+j[2])
                                    oc.config(text = "C)"+j[3])
                                    od.config(text = "D)"+j[4])
                                    
                                    count = count_
                                    
                                else:
                                    quiz_stu.destroy()


                            cont = Button(quiz_stu, text="Continue", width = 20, height=1, relief="ridge", borderwidth=5, command = update)
                            def mark():
                                if final_ans.get().lower() == j[5].lower():
                                    warning_quiz.config(text = "Correct Answer", fg = "green")
                                    cont.pack()
                                    
                                        
                                else:
                                    warning_quiz.config(text = "Wrong Answer", fg = "red")
                                    cont.pack()
                                    

                            submit = Button(quiz_stu, text="Submit", width = 20, height=1, relief="ridge", borderwidth=5, command = mark)
                            submit.pack()

                            warning_quiz = Label(quiz_stu, text = "", fg='red', font = ("Arial", 10))
                            warning_quiz.pack()
                            with open(fileopen, 'r', newline="") as f:
                                readerobj = csv.reader(f, delimiter="|")
                                readlst = list(readerobj)
                            
                            j = readlst[count]
                            ques.config(text = "Question:" + j[0])
                            oa.config(text = "A)"+j[1])
                            ob.config(text = "B)"+j[2])
                            oc.config(text = "C)"+j[3])
                            od.config(text = "D)"+j[4])

                            
                                        

                            
                            
                    else:
                        warninglbl = Label(fold, text = "Folder not found!", font = ('Courier', 10), fg='red')
                        warninglbl.pack()

                name_teach = Entry(fold)
                sub_teach = Entry(fold)
                name_teach.insert(0, "---Enter teacher name here---")
                sub_teach.insert(0, "---Enter Subject---")
                name_teach.pack()
                sub_teach.pack()
                fold_open = Button(fold, text = "Open Quiz folder", command = open_folder)
                fold_open.pack()
            

    find = Button(dropdwn, text = "Search", command = assigns)
    find.grid(row=0, column=1)


def check():
    log_result = login(user.get(), passw.get())
    warning_log.config(text = log_result)



def sign_up():
    try:
        stu.destroy()
    except:
        teach.destroy()
    s_p = Toplevel(root)
    s_p.title("Sign Up")
    s_p.geometry("500x500+700+300")
    s_p.iconphoto(False, icon)
    title_sp = Label(s_p, text = "Sign Up", height=5, font=("Courier", 15))
    title_sp.pack()

    u_name = Entry(s_p, width=30)
    u_name.insert(0, "Username")
    u_name.pack()

    password = Entry(s_p, width=30)
    password.insert(0, "Password")
    password.pack()

    pass_c = Entry(s_p, width=30)
    pass_c.insert(0, "Confirm Password")
    pass_c.pack()

    f_name = Entry(s_p, width=30)
    f_name.insert(0, "Full Name")
    f_name.pack()

    dob = Entry(s_p, width=30)
    dob.insert(0, "Date of Birth")
    dob.pack()

    cl_ = Entry(s_p, width=30)
    cl_.insert(0, "Class")
    cl_.pack()

    sec = Entry(s_p, width=30)
    sec.insert(0, "Section")
    sec.pack()

    pn = Entry(s_p, width=30)
    pn.insert(0, "Phone Number")
    pn.pack()

    gender = Entry(s_p, width=30)
    gender.insert(0, "Gender")
    gender.pack()
    
    add = Entry(s_p, width=30)
    add.insert(0, "Address")
    add.pack()
    
    
    warning = Label(s_p, text = "", fg='red', font = ("Arial", 10))
    warning.pack()
    def sp_add():
            #username, password, name, dob, class_, section, phone_number, gender, address
        if password.get() == pass_c.get():
            result = signup(u_name.get(), password.get(), f_name.get(), dob.get(), cl_.get(), sec.get(),pn.get(), gender.get(), add.get())
            warning.config(text=result) #not yet!! XD
            warning.config(fg = 'green')
        else:
            warning.config(text="Passwords do not match!")
            warning.config(fg = 'red')

        # lst = [u_name.get(), password.get(), f_name.get(), dob.get(), cl_sec.get(), add.get()]
        # with open("Credentials.txt", "a+") as f:
        #     flag = True
        #     creds_lst = f.readlines()
        #     print(creds_lst)
            
        #     for i in creds_lst:
        #         print(i)
        #         if lst[0] not in i:
        #             flag = True
        #         else:
        #             warning.config(text="User already registered!")
        #             warning.config(fg = 'red')
        #             flag = False
        #             break

        #     if flag == True:
        #         f.write("\n"+"   ".join(lst))
        #     else:
        #         pass
    sp_bt = Button(s_p, text="Sign Up", relief="flat", borderwidth=5, command = sp_add)
    sp_bt.pack()

def stu_log():
    root.wm_state('iconic')
    global stu
    stu = Toplevel(root)
    stu.title("Student Login")
    stu.geometry("500x500+700+300")
    stu.iconphoto(False, icon)
    title_stu = Label(stu, text = "Student Login", height=5, font=("Courier", 15))
    title_stu.pack()
    global user
    user = Entry(stu, width=30)
    user.insert(0, "Username")
    user.pack()
    global passw
    passw = Entry(stu, width=30)
    passw.insert(0, "Password")
    passw.pack()
    submit = Button(stu, text="Submit", width = 20, height=1, relief="ridge", borderwidth=5, command = check)
    submit.pack()
    sp = Label(stu, text = "Don't have an account?", font=("Courier", 12))
    sp.pack()
    sp_bt = Button(stu, text="Sign Up", relief="flat", borderwidth=5, command = sign_up)
    sp_bt.pack()
    global warning_log
    warning_log = Label(stu, text = "", fg='red', font = ("Arial", 10))
    warning_log.pack()






def quiz_upl(record_lst):
    # lvl = ""
    # def easyfunc():
    #     global lvl
    #     lvl = "Easy"
    #     diff_quiz.destroy()
    # def intermfunc():
    #     global lvl
    #     lvl = "Intermediate"
    #     diff_quiz.destroy()
    # def advancedfunc():
    #     global lvl
    #     lvl = "Advanced"
    #     diff_quiz.destroy()
    # diff_quiz  = Toplevel(root)
    # diff_quiz.title("Upload Quiz")
    # diff_quiz.geometry('700x700+700+300')

    # title_uq = Label(diff_quiz, text = "Choose Difficulty", height=5, font=("Courier", 15))
    # title_uq.pack()

    # easy = Button(diff_quiz, text="Easy", width = 20, height=1, relief="ridge", borderwidth=5, command = easyfunc)
    # intermediate = Button(diff_quiz, text="Intermediate", width = 20, height=1, relief="ridge", borderwidth=5, command = intermfunc)
    # advanced = Button(diff_quiz, text="Advanced", width = 20, height=1, relief="ridge", borderwidth=5, command = advancedfunc)
    # easy.pack()
    # intermediate.pack()
    # advanced.pack()

    # diff_quiz.mainloop()



    # print(record_lst)
    subj = record_lst[4]
    teach_name = record_lst[2]
    db = f"{teach_name}_{subj} Quiz\\" + "Quiz" + str(len(os.listdir(f"{teach_name}_{subj} Quiz")) + 1) + f"_{str(datetime.now())[:10]}" + ".csv"
    db_main = str(db)
    # print(db)
    # Question| Option A| Option B| Option C| Option D| Answer
    def quiz(filename=db_main):
        try:
            with open(filename, "r") as file:
                pass
        except:
            with open(filename, "w") as file:
                file.write("Question| Option A| Option B| Option C| Option D| Answer\n")
    quiz()
        # with open(filename, "r") as file:
        #     lines = file.readlines()
        #     # print(lines[0])
        #     headers = lines[0].split('|')
        #     records = [line.split('|') for line in lines[1:]]

        # questions = [record[0] for record in records]
        # ans = "yes"
        # global add_quiz
    def add_quiz(question, OA, OB, OC, OD, Answer, filename = db_main, ans = "yes"):
        if True:
            with open(filename, "r") as file:
                lines = file.readlines()
                # print(lines[0])
                headers = lines[0].split('|')
                records = [line.split('|') for line in lines[1:]]
            questions = [record[0] for record in records]
            question_exists = True
            while question_exists:
                # question = input("Enter question: ")
                if len(question) == 0:
                    warning_quiz.config(text = "question can't be empty")
                    break
                elif question in questions:
                    warning_quiz.config(text = "Question is already present")
                    break
                else:
                    warning_quiz.config(text = "")
                    question_exists = False
                    record = '|'.join([question, OA, OB, OC, OD, Answer, '\n'])
                    with open(filename, 'a') as file:
                        file.write(record)
            # OA = input("Enter option A: ")
            # OB = input("Enter option B: ")
            # OC = input("Enter option C: ")
            # OD = input("Enter option D: ")
            # Answer = input("Enter answer(A,B,C or D): ").upper()
            # ans = input("do you wanna continue?(yes or no): ").lower()
        

            
        if ans == "yes":
            ques.delete(0, END)
            ques.insert(0,"Enter Question")
            oa.delete(0, END)
            ob.delete(0, END)
            oc.delete(0, END)
            od.delete(0, END)
            oa.insert(0,"Enter Option A")
            ob.insert(0,"Enter Option B")
            oc.insert(0,"Enter Option C")
            od.insert(0,"Enter Option D")
            final_ans.delete(0, END)
            final_ans.insert(0, "Enter Answer(A,B,C or D)")
            ask_ans.delete(0, END)
        else:
            upl_quiz.destroy()

    upl_quiz = Toplevel(root)
    upl_quiz.title("Upload Quiz")
    upl_quiz.geometry('700x700+700+300')

    title_uq = Label(upl_quiz, text = "Upload Quiz", height=5, font=("Courier", 15))
    title_uq.pack()

    ques = Entry(upl_quiz)
    ques.insert(0,"Enter Question")
    ques.pack()

    frame_AB= Frame(upl_quiz)
    frame_AB.pack()
    oa = Entry(frame_AB)
    oa.insert(0,"Enter Option A")
    ob = Entry(frame_AB)
    ob.insert(0,"Enter Option B")
    oc = Entry(frame_AB)
    oc.insert(0,"Enter Option C")
    od = Entry(frame_AB)
    od.insert(0,"Enter Option D")
    oa.grid(row=0, column=0)
    ob.grid(row=0, column=1)
    oc.grid(row=1, column=0)
    od.grid(row=1, column=1)

    final_ans = Entry(upl_quiz)
    final_ans.insert(0, "Enter Answer(A,B,C or D)")
    final_ans.pack()

    ask_lbl = Label(upl_quiz, text = "Do you wish to add more questions after this?", fg='red', font = ("Arial", 10))
    ask_lbl.pack()

    ask_ans = Entry(upl_quiz)
    ask_ans.pack()

    submit = Button(upl_quiz, text="Submit Question", width = 20, height=1, relief="ridge", borderwidth=5, command = lambda: add_quiz(ques.get(), oa.get(), ob.get(), oc.get(), od.get(), final_ans.get().upper(), ans = ask_ans.get().lower()))
    submit.pack()

    warning_quiz = Label(upl_quiz, text = "", fg='red', font = ("Arial", 10))
    warning_quiz.pack()




    upl_quiz.mainloop()
    return

        # print("success")

def assign_upl(record_lst):
    filepath = filedialog.askopenfilename()
    # print("\n\n\n" + filepath)
    subj = record_lst[4]
    teach_name = record_lst[2]
    fileext = filepath.split('/')[-1].split('.')[-1]
    filename = f"{teach_name}_{subj} Assignment\\" + "Assignment" + str(len(os.listdir(f"{teach_name}_{subj} Assignment")) + 1) + f"_{str(datetime.now())[:10]}" + "." + fileext

    
    shutil.copy(filepath, filename)







def login_teach(username, password, filename = "db_teach.csv"):
    # username = username.strip()
    # password = password.strip()

    with open(filename, "r") as file:
        lines = file.readlines()
        records = [line.split('|') for line in lines[1:]]


    for record in records:
        if record[0] == username and record[1] == password:
            # print(username)
            teach.destroy()
            profile_teach(username)
            return "Login Successful"
            # return True
    return "Incorrect Username/Password"




def profile_teach(u_name):
    #extract things form database
    prof = Toplevel(root)
    prof.title("Profile")
    prof.geometry("1000x500+450+300")
    prof.iconphoto(False, icon)
    pers_details = Frame(prof, bg='black', height = 1080, width=480)
    pers_details.grid(row=0, column=0)
    # pic = Frame(pers_details, bg='white', height = 250, width=500)
    # pic.pack()
    lst = check_record(u_name, filename="db_teach.csv")
    # print(lst)
    # with open("Credentials.txt") as file:
    #     lst_temp = file.readline().split("    ")
    #     if lst_temp[0] == u_name:
    #         lst = lst_temp


    #username, password, name, dob, class_, section, phone_number, gender, address
    
    spaces_above = Label(pers_details, text = "\n\n\n\n\n\n", bg = 'black', fg = 'black')
    spaces_above.pack()

    name = Label(pers_details, text = f"Name: {lst[2]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    name.pack()

    dob = Label(pers_details, text = f"DOB: {lst[3]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    dob.pack()

    class_sec = Label(pers_details, text = f"Subject: {lst[4]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    class_sec.pack()

    gender = Label(pers_details, text = f"Gender: {lst[7]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    gender.pack()

    mobile = Label(pers_details, text = f"Mobile Number: +91 {lst[6]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    mobile.pack()

    address = Label(pers_details, text = f"Address: {lst[8]}", bg = 'black', fg = 'white', font=("Courier", 15)) ####
    address.pack()

    spaces_below = Label(pers_details, text = "\n"*25, bg = 'black', fg = 'black')
    spaces_below.pack()

    assign = Frame(prof, height = 1080)
    assign.grid(row = 0, column=1)

    # main_cont = Frame(assign)
    # main_cont.pack()

    dropdwn = Frame(assign, padx=800)
    dropdwn.pack()

    # options = ['Due', 'Completed']
    # result = StringVar()
    # result.set("--None--")
    # drop = OptionMenu(dropdwn, result, *options)
    # drop.grid(row=0, column=0)

    # drop_result = Frame(assign)
    # drop_result.pack()

    # default_result = Label(drop_result, text="Nothing to show.\nPlease select a choice", padx=650, font=("Courier", 15))
    # default_result.pack()



    # def assigns():
    #     if result.get() == "--None--":
    #         pass
    #     else:
    #         # print(result.get())
    #         default_result.config(text = f"{result.get()} Assignments")
    # find = Button(dropdwn, text = "Search", command = assigns)
    # find.grid(row=0, column=1)
    upl = Button(dropdwn, text="Upload assignment", width = 20, height=1, relief="ridge", borderwidth=5, command = lambda: assign_upl(lst))
    upl.pack()

    quiz = Button(dropdwn, text="Upload Quiz", width = 20, height=1, relief="ridge", borderwidth=5, command= lambda: quiz_upl(lst))
    quiz.pack()


def check_teach():
    log_result = login_teach(user_teach.get(), pass_teach.get())
    # user_teacher = str(user_teach.get())
    try:
        warning_log.config(text = log_result)
    except:
        pass




def sign_up_teach():
    try:
        stu.destroy()
    except:
        teach.destroy()
    s_p = Toplevel(root)
    s_p.title("Sign Up")
    s_p.geometry("500x500+700+300")
    s_p.iconphoto(False, icon)
    title_sp = Label(s_p, text = "Sign Up", height=5, font=("Courier", 15))
    title_sp.pack()

    u_name = Entry(s_p, width=30)
    u_name.insert(0, "Username")
    u_name.pack()

    password = Entry(s_p, width=30)
    password.insert(0, "Password")
    password.pack()

    pass_c = Entry(s_p, width=30)
    pass_c.insert(0, "Confirm Password")
    pass_c.pack()

    f_name = Entry(s_p, width=30)
    f_name.insert(0, "Full Name")
    f_name.pack()

    dob = Entry(s_p, width=30)
    dob.insert(0, "Date of Birth")
    dob.pack()

    global subject
    subject = Entry(s_p, width=30)
    subject.insert(0, "Subject")
    subject.pack()

    # sec = Entry(s_p, width=30)
    # sec.insert(0, "Section")
    # sec.pack()

    pn = Entry(s_p, width=30)
    pn.insert(0, "Phone Number")
    pn.pack()

    gender = Entry(s_p, width=30)
    gender.insert(0, "Gender")
    gender.pack()
    
    add = Entry(s_p, width=30)
    add.insert(0, "Address")
    add.pack()
    
    
    warning = Label(s_p, text = "", fg='red', font = ("Arial", 10))
    warning.pack()
    def sp_add():
            #username, password, name, dob, class_, section, phone_number, gender, address
        if password.get() == pass_c.get():
            result = signup(u_name.get(), password.get(), f_name.get(), dob.get(), subject.get(), "NIL",pn.get(), gender.get(), add.get(), filename="db_teach.csv")
            if result == "Signup successful":
                try:
                    os.mkdir(f"{f_name.get()}_"+ str(subject.get()) + " Assignments")
                    os.mkdir(f"{f_name.get()}_" + str(subject.get()) + " Quiz")
                except:
                    pass
            warning.config(text=result) #not yet!! XD
            warning.config(fg = 'green')
        else:
            warning.config(text="Passwords do not match!")
            warning.config(fg = 'red')

        # lst = [u_name.get(), password.get(), f_name.get(), dob.get(), cl_sec.get(), add.get()]
        # with open("Credentials.txt", "a+") as f:
        #     flag = True
        #     creds_lst = f.readlines()
        #     print(creds_lst)
            
        #     for i in creds_lst:
        #         print(i)
        #         if lst[0] not in i:
        #             flag = True
        #         else:
        #             warning.config(text="User already registered!")
        #             warning.config(fg = 'red')
        #             flag = False
        #             break

        #     if flag == True:
        #         f.write("\n"+"   ".join(lst))
        #     else:
        #         pass
    sp_bt = Button(s_p, text="Sign Up", relief="flat", borderwidth=5, command = sp_add)
    sp_bt.pack()



# user_teacher = ""

def teach_log():
    root.wm_state('iconic')
    global teach
    teach = Toplevel(root)
    teach.title("Teacher Login")
    teach.geometry("500x500+700+300")
    teach.iconphoto(False, icon)
    title_teach = Label(teach, text = "Teacher Login", height=5, font=("Courier", 15))
    title_teach.pack()
    global user_teach
    user_teach = Entry(teach, width=30)
    user_teach.insert(0, "Username")
    user_teach.pack()
    global pass_teach
    pass_teach = Entry(teach, width=30)
    pass_teach.insert(0, "Password")
    pass_teach.pack()
    # global user_person
    # user_person = str(user_teach.get())

    submit = Button(teach, text="Submit", width = 20, height=1, relief="ridge", borderwidth=5, command = check_teach)
    submit.pack()
    sp = Label(teach, text = "Don't have an account?", font=("Courier", 12))
    sp.pack()
    sp_bt = Button(teach, text="Sign Up", relief="flat", borderwidth=5, command = sign_up_teach)
    sp_bt.pack()
    global warning_log
    warning_log = Label(teach, text = "", fg='red', font = ("Arial", 10))
    warning_log.pack()

root = Tk()
root.title("Student Portal")
root.geometry("500x500+700+300")
root.configure(bg="yellow")
icon = PhotoImage(file="bbps.png")
root.iconphoto(False, icon)
title = Label(root, text = "Welcome to the Student Portal!",bg="#08999A",width=200,  height=5, font=("Courier", 15))
stud_login = Button(root, text="Student Login", width = 20, height=2, pady = 5, relief="ridge", font=("Courier", 15), borderwidth=5, command = stu_log)
teacher_login = Button(root, text="Teacher Login", width = 20, height=2, pady = 5, relief="ridge", font=("Courier", 15), borderwidth=5, command = teach_log)


title.pack()
stud_login.pack()
teacher_login.pack()
root.mainloop()
