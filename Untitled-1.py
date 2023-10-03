def create_file():
    f1 = open("para.txt", "w")
    print("Enter text for text file (enter blank line to stop): ")
    while True:
        s = input()
        if len(s) == 0:
            break
        else:
            f1.write(s + "\n")
    f1.close()

def count_space():
    f1 = open("para.txt")
    count = 0
    text = f1.read()
    for i in text:
        if i == " ":
            count+=1
        else:
            continue
    print(f"Number of blank spaces: {count}")
    f1.close()

create_file()
count_space()