#Class is
class Event:

    # Initialize the class with Event information
    def __init__(self, Name, Date, Description):

        self._Name = Name
        self._Date = Date
        self._Description = Description


    def __str__(self):
        return f"Event Name: {self._Name}, Date: {self._Date}, Description: {self._Description}"

    def getName(self):
        return self._Name

    def getDate(self):
        return self._Date

    def getDescription(self):
        return self._Description

    def setName(self, Name):
        self._Name = Name

    def setDate(self, Date):
        self.Date = Date

    def setDescription(self, Description):
        self._Description = Description


