class DoublyLinkedList:
    #Node class is used to store Events(element) in DoublyLinkedList
    class Node:
        def __init__(self, element, prev=None, next=None):
            # Parameters for Node class
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        # Parameters for DoublyLinkedList class
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)

        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    # Returns size of list
    def __len__(self):
        return self._size

    # Allows DoublyLinkedList to be iterable
    def __iter__(self):
        current = self._header._next
        while current is not self._trailer:
            yield current._element
            current = current._next

    # Returns True if list is empty otherwise false
    def isEmpty(self):
        return self._size == 0

    # Adds Event(element) to the end of the DoublyLinkedList
    def addEnd(self, element):
        newNode = self.Node(element, None, None)

        # If list is empty create get the header and trailer to point to newNode
        if self.isEmpty():
            newNode._prev = self._header
            self._header._next = newNode
            newNode._next = self._trailer
            self._trailer._prev = newNode
        else:
            # References trailer and final node in list
            trailer = self._trailer
            finalNode = trailer._prev

            # Links finalNode forward and back to newNode and points newNode forward and back to trailer
            finalNode._next = newNode
            newNode._prev = finalNode
            newNode._next = trailer
            trailer._prev = newNode
        self._size += 1

    # Returns the number of Events in DoublyLinkedList
    def numEvents(self):
        return self._size

    # Adds Event(element) to the beginning of the DoublyLinkedList
    def addBeginning(self, element):
        newNode = self.Node(element, None, None)
        if self.isEmpty():
            # If list is empty create get the header and trailer to point to newNode
            newNode._prev = self._header
            self._header._next = newNode
            newNode._next = self._trailer
            self._trailer._prev = newNode
        else:
            # references header and first node in list
            header = self._header
            firstNode = header._next

            # Links newNode forward and back to firstNode and points newNode forward and back to header
            newNode._next = firstNode
            firstNode._prev = newNode
            header._next = newNode
            newNode._prev = header
        self._size += 1

    def deleteLastNode(self):
        if self.isEmpty():
            return
        else:
            # In case there is only one node left in list(make header and trailer point to each other)
            if self._size == 1:
                self._header._next = self._trailer
                self._trailer._prev = self._header
            else:
                # Have trailer and secondLast Node point to each other and subtract one from the size
                lastNode = self._trailer._prev
                secondLastNode = lastNode._prev
                secondLastNode._next = self._trailer
                self._trailer._prev = secondLastNode
            self._size -= 1