import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        '''setup method called before any test is run. We create a new user asign value and test if its working fine'''
        self.user = User("STEVE", "123")


if __name__ == '__main__':
    unittest.main()