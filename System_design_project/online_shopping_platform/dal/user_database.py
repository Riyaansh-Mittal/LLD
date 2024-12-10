"""  
Singletion so that only one instance/object can be created

"""

class UserDatabase:
    _instance = None  # Class variable to hold the instance

    @staticmethod
    def create_instance():
        # Perform a check before creating an instance
        if not UserDatabase._instance:
            UserDatabase._instance = UserDatabase()
            return UserDatabase._instance
        else:
            print("Instance already exists. Cannot create another instance.")
            return UserDatabase._instance

    
