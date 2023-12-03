from User import User 
import access_control_policy as policy

def create_user(role: str) -> User:
    if role in policy.access_control_matrix:
        print("User with role {} created successfully".format(role))
        return User(role=role)
    print("{} does not exist as a role in the access control policy, user was not created".format(role))

if __name__ == "__main__":
    print("Welcome to the VeriGate system!\n-------------------------------")
    
    user1 = create_user("tech_support")

    # print(user1.get_permissions())
    # print(user1.role)
    user1.get_permissions_to_string()
    print(user1.get_client_access("premium_client"))
    user1.get_permissions_to_string()
    print(user1.revoke_client_access())
    user1.get_permissions_to_string()