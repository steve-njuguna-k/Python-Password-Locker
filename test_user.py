import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        '''setup method called before any test is run. We create a new user asign value and test if its working fine'''
        self.new_user = User("Steve", "12345")

    def test_init(self):
        self.assertEqual(self.new_user.username, "Steve")
        self.assertEqual(self.new_user.password, "12345")


if __name__ == '__main__':
    unittest.main()