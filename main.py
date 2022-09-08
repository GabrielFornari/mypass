
#from getpass import getpass
import sys
import os.path
import json

def main():
    userInterface = Interface()
    userFile = EncryptedFile("file.json")

    if not userFile.fileExists():
        if userInterface.checkNewUser():
            userFile.newFile()
        else:
            ErrorMessage.fileNotFound()
            return -1
    else:
        opt = userInterface.options(sys.argv)
        if opt > 0:
            # Check password
            if opt == 1:
                #data = {"name": "Gabriel", "age": 29}
                data = userInterface.newRegister()
                userFile.writeFile(data)
                return 0
            elif opt == 2:
                userFile.readFile()
                return 0
            elif opt == 3:
                pass # rm
                return 0
            elif opt == 4:
                pass # help
                return 0
        else:
            ErrorMessage.invalidInput()
            return -1


class EncryptedFile:
    def __init__(self, fileName) -> None:
        self._fileName = fileName
    
    def fileExists(self):
        if os.path.isfile(self._fileName):
            return True
        else:
            return False

    def newFile(self):
        try:
            with open(self._fileName, 'w', encoding='utf-8') as f:
                f.close()
        except FileNotFoundError:
            ErrorMessage.fileNotFound()

    def writeFile(self, data):
        try:
            with open(self._fileName, 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")
                f.close()
        except FileNotFoundError:
            ErrorMessage.fileNotFound()
            
    def readFile(self):
        try:
            with open(self._fileName, 'r') as f:
                data = []
                for line in f:
                    data.append(json.loads(line))
                print(data)
                f.close()
        except FileNotFoundError:
            ErrorMessage.fileNotFound()

class Interface:
    def newRegister(self):
        print("Title and Password cannot be empty. Pree ENTER to exit.")
        title = input("Title: ")
        login = input("Login: ")
        iPass = 0
        passwords = []
        password = input("Password "+str(iPass)+": ")
        while(password != ""):
            iPass += 1
            passwords.append(password)
            password = input("Password "+str(iPass)+": ")
        return {"title": title, "login": login, "passwords": passwords}

    def checkNewUser(self):
        userInput = input("Are you a new user? [Y/N] ")
        if userInput == "y" or userInput == "Y":
            return True
        else:
            return False

    def options(self, args):
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

class ErrorMessage:
    def fileNotFound():
        print("Error! File cound not be opened.")

    def invalidInput():
        print("Invalid input parameters. Check 'help' for more information.")

    


if __name__ == "__main__":
    main()