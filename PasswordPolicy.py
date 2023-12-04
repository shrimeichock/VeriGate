import re

class PasswordPolicy:
    def __init__(self):
        self.file = "weak_passwords.txt"

    def is_valid_password(self, username: str, password: str) -> bool:
        """
        Return true if password follows the password policy
        """
        length_condition = 8 <= len(password) <= 12
        character_condition = bool(re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)', password))
        match_username_condition = password != username
        weak_condition = not self.is_weak(password)
        common_condition = not self.is_common_format(password)
        
        if length_condition:
            if character_condition:
                if match_username_condition:
                    if weak_condition:
                        if common_condition:
                            return True
                        else:
                            print("ERROR - Password should not follow the format of calendar dates, license plate numbers, or telephone numbers")
                    else:
                        print("ERROR - Password is found in the list of weak passwords")
                else:
                    print("ERROR - Password cannot match username")
            else:
                print("ERROR - Password must contain at least one upper-case letter, one lower-case letter, one numerical digit, and one special character (!, @, #, $, %, ?, ∗, &)")
        else: 
            print("ERROR - Password must be 8-12 characters in length")

        return False 
    
    def is_common_format(self, password: str) -> bool:
        """
        Returns true if the password is in a date, license or phone number format
        """
        date_condition = bool(re.match(r'\d{1,2}[./-]\d{1,2}[./-]\d{2,4}', password)) 
        license_condition = bool(re.match(r'[A-Z0-9]{1,7}', password))
        phone_number_condition = bool(re.match(r'\d{3}[-.\s]?\d{3}[-.\s]?\d{4}', password))

        return date_condition and license_condition and phone_number_condition 


    def is_weak(self, password: str) -> bool:
        """
        Returns true if the password is is found in the list of common passwords
        """
        with open(self.file, 'r') as file:
            for line in file:
                if password in line:
                    return True
        return False