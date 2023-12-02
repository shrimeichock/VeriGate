import access_control_policy as policy

def get_permissions(role: str) -> dict:
    """ 
    Returns the permissions for a given role. If role does not exist, return None
    """
    if role in policy.access_control_matrix:
        return policy.access_control_matrix[role] 

def get_permissions_string(role: str) -> None:
    """
    Print the permissions for a given role as a formatted string
    """
    permissions = get_permissions(role)
    if type(permissions) == dict:
        for object, access in permissions.items():
            for i in access:
                print("- {} {}".format(i, object))
    else:
        print("ERROR: invalid role, does not exist in access control policy")

if __name__ == "__main__":
    print("Welcome to the VeriGate system!\n-------------------------------")
    get_permissions_string("premium_client")