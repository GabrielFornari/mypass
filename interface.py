

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

def chooseRegister(data):
    if not data:
        print("No register found in the database.")
        return

    print("Total number os entries recovered: " + str(len(data)))
    i = 1
    for register in data:
        print("[" + str(i) + "] " + register["title"])
        i += 1

    chosenIdx = int(input("Type entry number to choose: "))
    if chosenIdx > 0 and chosenIdx < len(data):
        return data[chosenIdx-1]
    else:
        return

def showHelp():
    print("Usage: mypass [OPTION] [KEY]")
    print("Stores and recovers passwords using encrypted JSON file.")
    print("Sort entries alphabetically.")
    print()
    print("   new: \t creates a new password entry")
    print("   ls: \t\t lists all saved password entries")
    print("   ls [KEY]: \t lists all password entries that matches KEY")
    print("   up [KEY]: \t edit password entry that matches KEY")
    print("   rm [KEY]: \t remove selected password entry that matches KEY")
    print("   help: \t show help")
    print()

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

def updateRegister(register):
    print("Update fields by typing new values.")
    print("  Title: " + register["title"])

    labels = register["labels"]
    values = register["values"]

    for i in range(len(register["labels"])):
        print("Original label name: " + register["labels"][i])
        label = input("New label name: ")
        if label != "":
            register["labels"][i] = label
        print("Original value: " + register["values"][i])
        value = input("New value: ")
        if value != "":
            register["values"][i] = value


def checkNewUser():
    userInput = input("Are you a new user? [Y/N] ")
    if userInput == "y" or userInput == "Y":
        return True
    else:
        return False

def checkOptions(args):
    if len(args) < 2 or len(args) > 3:
        return {"opt": "error"}
    if args[1] == "new":
        if len(args) == 2:
            return {"opt": "new"}
        else:
            return {"opt": "error"}
    elif args[1] == "ls":
        if len(args) == 2:
            return {"opt": "ls", "key": ""}
        elif len(args) == 3:
            return {"opt": "ls", "key": args[2]}
        else:
            return {"opt": "error"}
    elif args[1] == "rm":
        if len(args) == 2:
            return {"opt": "rm", "key": ""}
        elif len(args) == 3:
            return {"opt": "rm", "key": args[2]}
        else:
            return {"opt": "error"}
    elif args[1] == "up":
        if len(args) == 2:
            return {"opt": "up", "key": ""}
        elif len(args) == 3:
            return {"opt": "up", "key": args[2]}
        else:
            return {"opt": "error"}
    elif args[1] == "help":
        return {"opt": "help"}
    else:
        return {"opt": "error"}