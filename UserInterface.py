from PasswordManager import PasswordManager
from access_control_policy import access_control_matrix
from User import User
from PasswordPolicy import PasswordPolicy

class UserInterface:
    def __init__(self):
        self.manager = PasswordManager()
        self.policy = PasswordPolicy()

    def welcome_prompt(self):
        """
        Initial prompt asking user to login or register
        """
        
        print("Welcome to the VeriGate system!\n-------------------------------")
        print("(l) login \n(r) register")

        while True:
            user_input = input("Enter: ")

            if user_input == "l":
                self.login_prompt()
                break
            elif user_input == "r":
                self.register_prompt()
                break
            else:
                print("ERROR - Invalid option, please try again. Type 'l' or 'r'")

    def login_prompt(self):
        """
        Validate login info and show permissions if login was success. Otherwise allow retry
        """  
        print("\nLogin Page\n----------")
        username = input("Username: ")
        password = input("Password: ")
        if self.manager.verify_password(username, password):
            role = self.manager.retreive_record(username)[-1]
            print("\n----- Logged in as '{}' with role '{}' -----".format(username, role))
            self.display_user_account(role)
        else:
            print("ERROR - Invalid username and/or password\n")
            self.welcome_prompt()
    
    def register_prompt(self):
        """
        Validate given user info and add a new user to the system
        """
        print("\nRegister Page\n-------------")
        while True:
            username = input("Username: ")
            if self.manager.retreive_record(username) == None:
                break
            else:
                print("ERROR - A user with this name already exists in system")
        
        while True:
            password = input("Password: ")
            if self.policy.is_valid_password(username, password):
                break

        while True:
            print("Choose one of the following roles: ")
            for r in access_control_matrix.keys():
                print("  {}".format(r))
            role = input("Role: ")
            if role in access_control_matrix.keys():
                break
            else:
                print("ERROR - Invalid role, choose from the given options")
        
        self.manager.add_record(username, password, role)
        self.login_prompt()

    def display_user_account(self, role: str):
        """
        Show and manage the actions available for the user
        """
        user = User(role)
        user.get_permissions_to_string()
        print("  - type 'x' to logout\n")
        
        while True:
            user_input = input("Enter command: ")

            split_input = user_input.split()
            permision = split_input.pop(0)
            operation = " ".join(split_input)

            if user_input == "x":
                print("Logging out...\n")
                self.welcome_prompt()
                break
            elif (operation in user.get_permissions()) and (permision in user.get_permissions()[operation]):
                if operation == "privilege escalation":
                    escalate_role = self.privilege_escalation_menu(user)
                    if escalate_role:
                        self.display_user_account(escalate_role)
                else:
                    print("Performed '{}' operation".format(user_input))
            else:
                print("ERROR - Invalid command, try again")
    
    def privilege_escalation_menu(self, user: User) -> str:
        """
        Allow user to choose which client account they would like access to
        """
        user_account = input("Which user's account you would like access to? ")
        user_record = self.manager.retreive_record(user_account)
        if user_record and (user_record[-1] == "client" or user_record[-1] == "premium_client"):
            user.get_client_access(user_record)
            return user_record[-1]
        else:
            print("ERROR - Username is invalid or you do not have permission to access this account")

if __name__ == "__main__":
    gui = UserInterface()
    gui.welcome_prompt()
