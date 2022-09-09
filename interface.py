
def newRegister():
    print("Fields 'Title' and 'Password' cannot be empty.")
    title = input("Title: ")
    if title == "":
        return

    login = input("Login: ")

    iPass = 0
    passwordLabels = []
    passwords = []
    passwordLabel = input("Password label "+str(iPass)+": ")
    if passwordLabel == "":
        passwordLabel = "Password "+str(iPass)
    password = input(passwordLabel+": ")
    while(password != ""):
        passwords.append(password)
        passwordLabels.append(passwordLabel)
        iPass += 1
        passwordLabel = input("Password label "+str(iPass)+": ")
        if passwordLabel == "":
            passwordLabel = "Password "+str(iPass)
        password = input(passwordLabel+": ")
    if len(passwords) == 0:
        return
    else:
        return {"title": title, "login": login, "passwordLabels": passwordLabels, "passwords": passwords}

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