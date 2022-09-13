
#from getpass import getpass
from email import message
import sys
import os.path
import json

import interface
import messages as msg

def main():
    userFile = EncryptedFile("file.json")

    if not userFile.fileExists():
        if interface.checkNewUser():
            userFile.createFile()
        else:
            msg.fileNotFound()
            return -1
    else:
        userChoice = interface.checkOptions(sys.argv)
        if userChoice["opt"] == "error":
            msg.invalidInput()
            return -1
        else:
            # Check password
            if userChoice["opt"] == "new":
                register = interface.newRegister()
                if register:
                    userFile.writeFile(register)
                return 0
            elif userChoice["opt"] == "ls":
                data = userFile.readFile(userChoice["key"])
                interface.showRegisters(data)
                return 0
            elif userChoice["opt"] == "rm":
                data = userFile.readFile(userChoice["key"])
                register = interface.chooseRegister(data)
                if userFile.removeRegister(register):
                    msg.successfulRemoved()
                    return 0
                else:
                    msg.invalidInput()
                    return -1
            elif userChoice["opt"] == "up":
                data = userFile.readFile(userChoice["key"])
                register = interface.chooseRegister(data)
                interface.updateRegister(register)
                
                userFile.updateRegister(register)

                print(register)

                # Search for 'key'
                # Show results and confirm choice
                # Ask for new labels/fields
                # Update
                return 0
            elif userChoice["opt"] == "help":
                interface.showHelp()
                return 0
            else:
                # Unexpected error
                return -2


class EncryptedFile:
    def __init__(self, fileName) -> None:
        self._fileName = fileName
    
    def fileExists(self):
        if os.path.isfile(self._fileName):
            return True
        else:
            return False

    def createFile(self):
        try:
            with open(self._fileName, 'w', encoding='utf-8') as f:
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()

    def writeFile(self, data):
        try:
            with open(self._fileName, 'a', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
                f.write("\n")
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()

    def readFile(self, key = ""):
        try:
            with open(self._fileName, 'r', encoding='utf-8') as f:
                data = []
                for line in f:
                    title = json.loads(line)["title"]
                    if key.casefold() in title.casefold():
                        data.append(json.loads(line))
                f.close()
                return data
        except FileNotFoundError:
            msg.fileNotFound()

    def removeRegister(self, register):
        if not register:
            return 0
        try:
            with open(self._fileName, 'r', encoding='utf-8') as f:
                data = []
                for line in f:
                    title = json.loads(line)["title"]
                    if register["title"] != title:
                        data.append(json.loads(line))
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()
        
        try:
            with open(self._fileName, 'w', encoding='utf-8') as f:
                for register in data:
                    json.dump(register, f, ensure_ascii=False)
                    f.write("\n")
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()

        return 1

    def updateRegister(self, register):
        if not register:
            return 0
        try:
            with open(self._fileName, 'r', encoding='utf-8') as f:
                data = []
                for line in f:
                    title = json.loads(line)["title"]
                    if register["title"] == title:
                        data.append(register)
                    else:
                        data.append(json.loads(line))
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()

        try:
            with open(self._fileName, 'w', encoding='utf-8') as f:
                for register in data:
                    json.dump(register, f, ensure_ascii=False)
                    f.write("\n")
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()

        return 1

if __name__ == "__main__":
    main()