# models folder exists to store class files for generating objects in python and passing them to SQL
class User:
    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
