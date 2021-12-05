class User:
    user_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        cls.user_list

    @classmethod
    def verify_user(cls, username, password):
        for user in cls.user_list:
            if (user.username == username and user.password == password):
                return user