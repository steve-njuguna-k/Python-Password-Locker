class User:
    '''User list for storing new user information'''
    user_list = []

    def __init__(self, username, password):
        '''Function to define User class properties'''
        self.username = username
        self.password = password

    def save_user(self):
        '''Function to store new user info into the user list'''
        User.user_list.append(self)

    def delete_user(self):
        '''Function to delete user info from the user list'''
        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        '''Function to display user specific information'''
        return cls.user_list

    @classmethod
    def verify_user(cls, username, password):
        '''Function to verify user info existence during log in'''
        for user in cls.user_list:
            if (user.username == username and user.password == password):
                return user