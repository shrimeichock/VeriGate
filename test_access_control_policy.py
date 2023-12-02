import unittest
from main import get_permissions, get_permissions_string
from access_control_policy import access_control_matrix

class TestAccessControlPolicy(unittest.TestCase):

    def test_valid_roles(self):
        """
        Test that valid roles are returning the correct dictionaries
        """
        self.assertEqual(get_permissions("client"), {
        "client info": ["view", "modify"],
        "balance": ["view"],
        "investment portfolio": ["view"],
        "financial advisor info": ["view"],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
        })
        self.assertEqual(get_permissions("investment_analyst"),{
        "client info": ["view"],
        "balance": ["view"],
        "investment portfolio": ["view", "modify"],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": ["view", "modify"],
        "money market instruments": ["view"],
        "private consumer instruments": ["view"],
        "derivatives trading": ["view"],
        "interest instruments": ["view"]
    })
        self.assertEqual(get_permissions("tech_support"), {
        "client info": ["view"],
        "balance": [],
        "investment portfolio": [],
        "financial advisor info": [],
        "financial planner info": [],
        "investment analyst info": [],
        "money market instruments": [],
        "private consumer instruments": [],
        "derivatives trading": [],
        "interest instruments": []
        })

    def test_invalid_roles(self):
        """
        Check that invalid roles return an error
        """
        self.assertEqual(get_permissions("invalid_role"), None)
        self.assertEqual(get_permissions("client_1"), None)

    def test_only_access_allowed(self):
        """
        Check that the user cannot access resources outside of what their permissions allow
        """
        self.assertEqual(get_permissions("client")["investment analyst info"], [])
        self.assertEqual(get_permissions("teller")["investment portfolio"], ["view"])
        self.assertEqual(get_permissions("compliance_officer")["investment portfolio"], ["view", "validate"])

if __name__ == '__main__':
    unittest.main()
