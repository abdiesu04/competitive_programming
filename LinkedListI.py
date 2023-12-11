class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addBeg(self , val):
        node = Node (val)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
    def addEnd(self,value):
        node  = Node (value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def printALl(self):
        temp = self.head
        while temp != None:
        print(temp.data)
            temp = temp.next
