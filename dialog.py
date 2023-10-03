# import tkinter as tk
# from tkinter import filedialog
# import shutil
# root = tk.Tk()
# filepath = filedialog.askopenfilename(initialdir="Bhavna Mittal_Computer Science Assignment")
# # print("\n\n\n" + filepath)

# filename = filepath.split('/')[-1]
# print(filename.split('.')[-1])
# shutil.copy(filepath, "Bhavna Mittal_Computer Science Assignment\\" + filename)
# root.mainloop()


# # import os
# # print(os.listdir("./"))

# import csv
# with open('db.csv', 'r', newline="") as f:
#     readerobj = csv.reader(f, delimiter="|")
#     for i in readerobj:
#         print(i)

count1 = 0
def func():
    # global count1
    # count1 = 2
    def func_():
        global count1
        count1 = count1 + 1
        print(count1)
    func_()
    # func_()
    # func_()
    # func_()


func()