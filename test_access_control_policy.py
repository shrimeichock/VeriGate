import unittest
from User import User
import main
from access_control_policy import access_control_matrix
from datetime import time

class TestAccessControlPolicy(unittest.TestCase):

    def test_valid_roles(self):
        """
        Test that valid roles are returning the correct dictionaries
        """
        user1 = main.create_user("client")
        self.assertEqual(user1.get_permissions(), {
        "client info": ["view", "modify"],
        "balance": ["view"],
        "investment portfolio": ["view"],
        "financial advisor info": ["view"],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": [],
        "privilege escalation": []
        })
        user2 = main.create_user("investment_analyst")
        self.assertEqual(user2.get_permissions(),{
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view", "modify"],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": ["view", "modify"],
        "money market instruments": ["view"],
        "private consumer instruments": ["view"],
        "derivatives trading": ["view"],
        "interest instruments": ["view"],
        "privilege escalation": []
        })
        user3 = main.create_user("tech_support")
        self.assertEqual(user3.get_permissions(), {
        "client info": ["view"],
        "balance": [],
        "investment portfolio": [],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": [],
        "privilege escalation": ["execute"]
        })

    def test_invalid_roles(self):
        """
        Check that invalid roles return an error
        """
        user1 = main.create_user("invalid_role")
        self.assertEqual(user1, None)
        # self.assertEqual(get_permissions("client_1"), None)

    def test_only_access_allowed(self):
        """
        Check that the user cannot access resources outside of what their permissions allow
        """
        user1 = main.create_user("client")
        user2 = main.create_user("teller")
        user3 = main.create_user("compliance_officer")
        self.assertEqual(user1.get_permissions()["investment analyst info"], [])
        self.assertEqual(user2.get_permissions()["investment portfolio"], ["view"])
        self.assertEqual(user3.get_permissions()["investment portfolio"], ["view", "validate"])

    def test_esclate_privileges(self):
        """
        Check that only the tech support user can escalate their privileges and that they can only access client and premium_client
        """
        user1 = main.create_user("client")
        user2 = main.create_user("tech_support")
        self.assertEqual(user1.get_client_access("client"), None)
        self.assertEqual(user2.get_client_access("client"), "Tech support now has access to client's account")
        self.assertEqual(user2.get_permissions(), access_control_matrix["client"])
        self.assertEqual(user2.get_client_access("premium_client"), "Tech support now has access to premium_client's account")
        self.assertEqual(user2.get_permissions(), access_control_matrix["premium_client"])
        self.assertEqual(user2.get_client_access("compliance_officer"), None)
        self.assertEqual(user2.get_permissions(), access_control_matrix["premium_client"])

    def test_revoke_privileges(self):
        """
        Check that only tech_support can have their privileges revoked and that their access rights return to the expected value
        """
        user1 = main.create_user("investment_analyst")
        user2 = main.create_user("tech_support")
        self.assertEqual(user1.revoke_client_access(), None)
        self.assertEqual(user2.get_client_access("client"), "Tech support now has access to client's account")
        self.assertEqual(user2.get_permissions(), access_control_matrix["client"])
        self.assertEqual(user2.revoke_client_access(), "Access to client account has been revoked")
        self.assertEqual(user2.get_permissions(), access_control_matrix["tech_support"])

    def test_teller_access(self):
        """
        Check that teller can only access the system within the allowed hours
        """
        time1 = time(9, 0, 0)  # 9am
        time2 = time(17, 0, 0)  # 5pm
        time3 = time(1, 0, 0)  # 1am
        time4 = time(13, 0, 0)  # 1pm
        user1 = main.create_user("teller")
        self.assertTrue(user1.check_teller_access(time1))
        self.assertTrue(user1.check_teller_access(time2))
        self.assertFalse(user1.check_teller_access(time3))
        self.assertTrue(user1.check_teller_access(time4))
        
if __name__ == '__main__':
    unittest.main()
