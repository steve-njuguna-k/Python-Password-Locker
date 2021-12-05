import string
from random import choice

class Credentials:
    credentials_list = []

    def __init__(self, accountName, accountUsername, accountPassword):
        self.accountName = accountName
        self.accoutnUsername = accountUsername
        self.accountPassword = accountPassword

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    @classmethod
    def generate_password(cls):
        characters = string.ascii_letters + string.digits
        password = "".join(choice(characters) for x in range(0,16))
        cls.password = password
        return password

    @classmethod
    def verify_credentials_exist(cls, accountName):
        for credential in cls.credentials_list:
            if credential.accountName == accountName:
                return True
            return False

    @classmethod
    def search_credentials(cls, accountName):
        for credential in cls.credentials_list:
            if credential.accountName == accountName:
                return credential