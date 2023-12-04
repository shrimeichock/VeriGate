import hashlib
import uuid

class PasswordManager:
    def __init__(self):
        self.file = "passwd.txt"
        self.salt_size = 32
        self.num_iterations = 100

    def add_record(self, userid: str, password: str, role: str) -> None:
        """
        Add the given record to the password file
        """
        salt = self.create_salt()

        with open(self.file, 'a') as file:
            file.write("{}:{}:{}:{}\n".format(userid, salt, self.create_salted_hash(salt, password), role))

    def retreive_record(self, userid: str) -> list:
        """
        Returns the record for a given user in password file
        """
        with open(self.file, 'r') as file:
            for line in file:
                separated = line.strip("\n").split(':')
                if userid in separated:
                    return separated

    def create_salt(self) -> str:
        """
        Returns a randomly generated salt
        """
        return uuid.uuid4().hex[:self.salt_size] 

    def create_salted_hash(self, salt: str, password: str) -> str:
        """
        Returns the password hashed with the salt
        """
        hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), self.num_iterations).hex()

        return hash
    
    def verify_password(self, user:str, password: str) -> bool:
        """
        Return true if the hash of the given password and salt for that user matches what is saved in the file
        """
        record = self.retreive_record(user)

        if record:
            salt = record[1]
            saved_hash = record[2]

            new_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), self.num_iterations).hex()

            return saved_hash == new_hash
        
        return False

