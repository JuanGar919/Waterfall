# Creates an Event object that holds all the information obtained from the GoogleAPI class
class Event:

    # Initializing the class with Event information
    def __init__(self, Name, DateTime, Description):

        self._Name = Name
        self._DateTime = DateTime
        self._Description = Description


    # Returns Event information in format
    def __str__(self):
        return f"Event Name: {self._Name}, Date: {self._DateTime}, Description: {self._Description}"

    # Allows user to obtain Name
    def getName(self):
        return self._Name

    # Allows user to obtain DateTime
    def getDateTime(self):
        return self._DateTime

    # Allows user to obtain Description
    def getDescription(self):
        return self._Description

    # Allows user to set Name for Event
    def setName(self, Name):
        self._Name = Name

    # Allows user to set DateTime for Event
    def setDateTime(self, DateTime):
        self.DateTime = DateTime

    # Allows user to set Description for Event
    def setDescription(self, Description):
        self._Description = Description




