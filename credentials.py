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