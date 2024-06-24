class User:
    def __init__(self, first_name, last_name):
        self.fname = first_name
        self.lname = last_name
    
    def printFirstName(self):
        print(self.fname)

    def printLastName(self):
        print(self.lname)

    def printAllName(self):
        print(self.fname, self.lname)