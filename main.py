
#from getpass import getpass
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
        opt = interface.checkOptions(sys.argv)
        if opt > 0:
            # Check password
            if opt == 1:
                data = interface.newRegister()
                if data:
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
            msg.invalidInput()
            return -1


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
            
    def readFile(self):
        try:
            with open(self._fileName, 'r') as f:
                data = []
                for line in f:
                    data.append(json.loads(line))
                print(data)
                f.close()
        except FileNotFoundError:
            msg.fileNotFound()



if __name__ == "__main__":
    main()