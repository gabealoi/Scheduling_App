'''
    This is an object class to encapsulate the information that will be grabbed from the Postgres database.
    It's methods will be used to set and retrieve information about all of the existing employees
'''

class Employee:
    # Constructor
    def __init__(self, id, name, age, hours):
        self.id = id
        self.name = name
        self.age = age
        self.hours = hours

    
    # getters
    def getID(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getHours(self):
        return self.hours
    

    # toString override
    def __str__(self) -> str:
        return f"{self.id}\n{self.name}\n{self.age}\n{self.hours}\n"
    
        