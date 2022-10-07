
#from getpass import getpass
import sys
import os.path

import cryptfile
import interface
import messages as msg

def main():
    userFile = cryptfile.EncryptedFile()

    if not userFile.fileExists():
        if interface.checkNewUser():
            newPassword = interface.createPassword()
            if newPassword == -1:
                return 0
            userFile.setPassword(newPassword)
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
            # Warning: no password check!
            
            userFile.setPassword(interface.getPassword())
            if userChoice["opt"] == "new":
                register = interface.newRegister()
                if register:
                    userFile.updateFile(register)
                return 0
            elif userChoice["opt"] == "ls":
                data = userFile.readFileFilter(userChoice["key"])
                interface.showRegisters(data)
                return 0
            elif userChoice["opt"] == "rm":
                data = userFile.readFileFilter(userChoice["key"])
                register = interface.chooseRegister(data)
                if userFile.removeRegister(register) > 0:
                    msg.successfullyRemoved()
                    return 0
                else:
                    msg.invalidInput()
                    return -1
            elif userChoice["opt"] == "up":
                data = userFile.readFileFilter(userChoice["key"])
                register = interface.chooseRegister(data)
                interface.updateRegister(register)
                if userFile.updateRegister(register) > 0:
                    msg.successfullyUpdated()
                    return 0
                else:
                    msg.invalidInput()
                    return -1
            elif userChoice["opt"] == "help":
                interface.showHelp()
                return 0
            elif userChoice["opt"] == "import":
                if userFile.importFile(userChoice["filename"]) > 0:
                    msg.successfullyImported()
                    return 0
                else:
                    msg.invalidInput()
                    return -1
            else:
                # Unexpected error
                return -2


if __name__ == "__main__":
    main()