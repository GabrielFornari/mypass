

def showRegisters(data):
    if not data:
        print("There is no register in the database.")
        return

    print("Total number os entries recovered: " + str(len(data)))
    print("--------------------")
    for register in data:
        print("Title: " + register["title"])
        for i in range(len(register["labels"])):
            print("   " + register["labels"][i] + ": " + register["values"][i])
        print("--------------------")



def newRegister():
    print("Fields 'Title' and 'Password' cannot be empty.")
    title = input("Title: ")
    if title == "":
        return

    labels = []
    values = []
    label = input("Label name: ")
    while(label != ""):
        value = input(label+": ")
        labels.append(label)
        values.append(value)
        label = input("Label name: ")
        
    if len(values) == 0:
        return
    else:
        return {"title": title, "labels": labels, "values": values}

def checkNewUser():
    userInput = input("Are you a new user? [Y/N] ")
    if userInput == "y" or userInput == "Y":
        return True
    else:
        return False

def checkOptions(args):
    if len(args) < 2 or len(args) > 3:
        return -1
    if args[1] == "new":
        return 1
    elif args[1] == "ls":
        return 2
    elif args[1] == "rm":
        return 3
    elif args[1] == "help":
        return 4
    else:
        return -1