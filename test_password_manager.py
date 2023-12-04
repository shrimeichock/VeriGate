import unittest
import os
from PasswordManager import PasswordManager

class TestAccessControlPolicy(unittest.TestCase):

    def test_add_record(self):
        """
        Check that records are being added to password file
        """
        filename = "sample.txt"
        user1 = "user1"
        role1 = "client"
        manager = PasswordManager(filename)
        manager.add_record(user1, "password1", role1)
        
        with open(filename, 'r') as file:
            for line in file:
                separated = line.strip("\n").split(':')
                if user1 in separated:
                    self.assertEqual(separated[0], user1) # check that userid in file is same
                    self.assertEqual(separated[-1], role1) # check that role in file is same
        os.remove(filename) # delete file after test runs

    def test_retrieve_record(self):
        """
        Check that the correct record is being retrieved
        """
        filename = "sample.txt"
        user1 = "user1"
        role1 = "client"
        password1 = "password1"
        user2 = "user2"
        manager = PasswordManager(filename)
        manager.add_record(user1, password1, role1) # two users only differing in username
        manager.add_record(user2, password1, role1)

        with open(filename, 'r') as file:
            lines = file.readlines()

            line1 = lines[0].strip("\n").split(':')
            line2 = lines[1].strip("\n").split(':')

        self.assertEqual(manager.retreive_record(user1), line1) # check that retrived user is first line in file
        self.assertEqual(manager.retreive_record(user2), line2)
    
        os.remove(filename) # delete file after test runs

if __name__ == '__main__':
    unittest.main()