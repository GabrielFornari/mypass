
import os.path
import json

from cryptography.fernet import Fernet
import bcrypt
import base64


class EncryptedFile:
    def __init__(self) -> None:
        self._fileName = ".dat"
    
    def setPassword(self, psw):
        # generate Fernet key
        key = bcrypt.kdf(password=psw, salt=b'salt', desired_key_bytes=32, rounds=100)
        self.__password = base64.b64encode(key)

    def fileExists(self):
        if os.path.isfile(self._fileName):
            return True
        else:
            return False

    def createFile(self):
        f = Fernet(self.__password)
        encryptedData = f.encrypt(b"[]")
        try:
            with open(self._fileName, 'wb') as file:
                file.write(encryptedData)
                file.close()
        except FileNotFoundError:
            return -1
        return 1

    def updateFile(self, register):
        if not register:
            return -2
        registers = self.readFile()
        registers.append(register)
        jsonObj = json.dumps(registers, ensure_ascii=False)
        f = Fernet(self.__password)
        encryptedData = f.encrypt(jsonObj.encode('utf-8'))
        try:
            with open(self._fileName, 'wb') as file:
                file.write(encryptedData)
                file.close()
        except FileNotFoundError:
            return -1
        return 1

    def importFile(self, fileName):
        try:
            with open(fileName, 'r', encoding='utf-8') as file:
                registers = json.load(file)
                file.close()
        except FileNotFoundError:
            return -1
        for register in registers:            
            self.updateFile(register)
        return 1

    def readFile(self):
        try:
            with open(self._fileName, 'rb') as file:
                encryptedData = file.read()
                file.close()
        except FileNotFoundError:
            return -1
        f = Fernet(self.__password)
        jsonObj = f.decrypt(encryptedData).decode('utf-8')
        return json.loads(jsonObj)

    def readFileFilter(self, key = ""):
        registers = self.readFile()
        out = []
        for register in registers:
            title = register["title"]
            if key.casefold() in title.casefold():
                out.append(register)
        return out

    def removeRegister(self, register):
        if not register:
            return -2
        registers = self.readFile()
        try:
            registers.remove(register)
        except:
            return -3
        jsonObj = json.dumps(registers, ensure_ascii=False)
        f = Fernet(self.__password)
        encryptedData = f.encrypt(jsonObj.encode('utf-8'))
        try:
            with open(self._fileName, 'wb') as file:
                file.write(encryptedData)
                file.close()
        except FileNotFoundError:
            return -1
        return 1

    def updateRegister(self, register):
        if not register:
            return -2
        registers = self.readFile()
        
        for i in range(0, len(registers)):
            if registers[i]["title"] == register["title"]:
                registers[i] = register

        jsonObj = json.dumps(registers, ensure_ascii=False)
        f = Fernet(self.__password)
        encryptedData = f.encrypt(jsonObj.encode('utf-8'))
        try:
            with open(self._fileName, 'wb') as file:
                file.write(encryptedData)
                file.close()
        except FileNotFoundError:
            return -1
        return 1
        