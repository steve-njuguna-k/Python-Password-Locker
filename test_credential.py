import unittest
from credentials import Credentials

class TestCredential(unittest.TestCase):
    def setUp(self):
        '''setup method called before any test is run. We create a new credential asign value and test if its working fine'''
        self.new_credential = Credentials("IG", "STEVE", "12345")

if __name__ == "__main__":
    unittest.main()