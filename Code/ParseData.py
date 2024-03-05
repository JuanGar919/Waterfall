from DoublyAccLinkedList import DoublyLinkedList
from GoogleAPI import main
from Event import Event

googleData = main()
def ParseList(googleEvent):
    doublyEventLinkedList = DoublyLinkedList()

    for event in googleData:
        eventData = event.split("/")

        name = eventData[0].strip()
        date = eventData[1].strip()
        description = eventData[2].strip()

        event = Event(name, date, description)

        doublyEventLinkedList.addEnd(event)


    return doublyEventLinkedList



dll = ParseList(googleData)

for x in dll:
    print(x)