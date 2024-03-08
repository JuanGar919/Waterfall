from DoublyEventLinkedList import DoublyLinkedList
from GoogleAPI import getCalendarEvents
from Event import Event

googleData = getCalendarEvents()
def ParseList(googleEvent):
    # Creating doublyLinkedList to store all events
    doublyEventLinkedList = DoublyLinkedList()

    #Go through all list of googleData and parse each element seperated by '/' and then store each element in the list to an Event object
    for event in googleData:
        eventData = event.split("/")

        #Grabs first second and third element seperated by '/'
        name = eventData[0].strip()
        date = eventData[1].strip()
        description = eventData[2].strip()

        event = Event(name, date, description)

        doublyEventLinkedList.addEnd(event)

    return doublyEventLinkedList

