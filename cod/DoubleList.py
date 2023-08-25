from Node import *

class DoubleList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.length= 0

    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if(self.head==None):
            self.head = self.tail = newNode
        else:
            newNode.prev=None
            newNode.next=self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def insertAtEnd(self,data):
        newNode = Node(data, None, None)
        if (self.head==None):
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.length +=1

    def insertAtGivenPosition(self, pos, data):
        if self.head == None or pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif pos < self.length:
            curr = self.head
            count = 0
            while curr != None and count < pos:
                curr = curr.next
                count += 1
            newNode = Node(data, None, None)
            newNode.next = curr.next
            newNode.prev = curr.prev
            curr.next = newNode
        self.length += 1

    def printAll(self):
        if(self.head == None):
            print("no data")
        else:
            while self.head != None:
                print(self.head.data)
                self.head = self.head.next

    def removeAtBeginning(self):
        if self.length == 1:
            self.head=self.tail=None
            self.length -=1
        else:
            next = self.head.next
            next.prev = None
            self.head = next
            self.length -=1            

    def removeAtEnd(self):
        if self.length == 1:
            self.head=self.tail=None
            self.length = 0
        else:
            prev = self.tail.prev
            prev.next = None
            self.tail = prev
            self.length -=1