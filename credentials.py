import string
from random import choice

class Credentials:
    '''Credential list for storing new credential information'''
    credentials_list = []

    def __init__(self, accountName, accountUsername, accountPassword):
        '''Function to define Credential class properties'''
        self.accountName = accountName
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword

    def save_credentials(self):
        '''Function to store new credential info into the credential list'''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''Function to delete saved credential info from the credential list'''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''Function to display credential specific information'''
        return cls.credentials_list

    @classmethod
    def generate_password(cls):
        '''Function to auto generate credential password'''
        characters = string.ascii_letters + string.digits
        password = "".join(choice(characters) for x in range(0,16))
        cls.password = password
        return password

    @classmethod
    def verify_credential_exist(cls, accountName):
        '''Function to verify credential info existence during search or display'''
        for credential in cls.credentials_list:
            if credential.accountName == accountName:
                return True
            return False

    @classmethod
    def search_saved_credential(cls, accountName):
        '''Function to search for credential info existence during search or display'''
        for credential in cls.credentials_list:
            if credential.accountName == accountName:
                return credential