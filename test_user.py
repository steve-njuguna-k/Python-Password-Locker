import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        '''setup method called before any test is run. We create a new user asign value and test if its working fine'''
        self.new_user = User("Steve", "12345")

    def test_init(self):
        ''''method runs whenever we instanciate our class so every time we instanciate our class we create a user'''
        self.assertEqual(self.new_user.username, "Steve")
        self.assertEqual(self.new_user.password, "12345")

    def tearDown(self):
        '''run after every test to ensure user list never conflicts'''
        User.user_list = []

    def test_saveUser(self):
        ''''we save user then assert if it exist in  user list'''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_displayUser(self):
        pass


if __name__ == '__main__':
    unittest.main()