import access_control_policy as policy
from datetime import datetime, time

class User:
    def __init__(self, role: str):
        self.role = role
        self.permissions = policy.access_control_matrix[role] #TODO

    def get_permissions(self) -> dict:
        """ 
        Returns the permissions for the user's role
        """
        current_time = datetime.now().time()
        
        if self.role == "teller":
            if self.check_teller_access(current_time):
                self.permissions = policy.access_control_matrix[self.role]
            else: 
                self.permissions = {}
                print("ERROR: Tellers only have access to the system between 9am to 5pm")
        return self.permissions
    
    def check_teller_access(self, current_time: time) -> bool:
        """
        Return true if teller can access system
        """
        min_time = time(9, 0, 0)  # 9am
        max_time = time(17, 0, 0)  # 5pm

        if min_time <= current_time <= max_time:
            return True
        return False

    def get_permissions_to_string(self) -> None:
        """
        Print the permissions for the user's role as a formatted string
        """
        for object, access in self.permissions.items():
            for i in access:
                print("- {} {}".format(i, object))

    def get_client_access(self, client_role: str) -> str:
        """
        If the user has rights to get client access, escalate their permissions to that of the client they are requesting
        This operation is only accessible to users with the tech_support role.
        """
        if policy.access_control_matrix[self.role]["privilege escalation"] == ["execute"] and client_role in ["client", "premium_client"]:
            self.permissions = policy.access_control_matrix[client_role] 
            return "Tech support now has access to {}'s account".format(client_role)
       
    def revoke_client_access(self) -> str:
        """
        If the user has revoke access rights, revert to their original permissions.
        This operation is only accessible to users with the tech_support role.
        """
        if policy.access_control_matrix[self.role]["privilege escalation"] == ["execute"]:
            self.permissions = policy.access_control_matrix[self.role] #TODO use set permisions
            return "Access to client account has been revoked"
