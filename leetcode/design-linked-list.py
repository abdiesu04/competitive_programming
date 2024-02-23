class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            node = Node(val)
            prev_node = self.head
            for i in range(index-1):
                prev_node = prev_node.next
            next_node = prev_node.next
            prev_node.next = node
            node.prev = prev_node
            node.next = next_node
            next_node.prev = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.head
            for i in range(index):
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1