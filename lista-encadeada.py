class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.length = 0
        self.head = None

    def insertBeginning(self,data):
        node = Node(data)
        if self.length == 0:
            self.head = node
            self.length = 1
            return
        node.next = self.head
        self.head = node
        self.length += 1

    def printList(self):
        node_aux = self.head
        while node_aux != None:
            print(node_aux.data)
            node_aux = node_aux.next

    def getLength(self):
        return self.length

    def insertEnd(self,data):
        node = Node(data)
        node_aux = self.head
        if self.length == 0:
            self.insertBeginning(data)
            return
        while node_aux.next != None:
            node_aux = node_aux.next
        node_aux.next = node
        self.length += 1

    def insertPosisition(self, data, pos):
        if pos > self.length:
            return 'posição invalida'
        node = Node(data)
        node_aux = self.head
        count = 0
        while count < pos - 1:
            count +=1
            node_aux = node_aux.next
        node.next = node_aux.next
        node_aux.next = node
        self.length += 1

    def fullForce(self,n):
        position = 0
        node_aux = self.head
        while node_aux.next != None:
            position += 1
            node_aux = node_aux.next
        target = position - (n + 1)
        count = 0
        node_aux = self.head
        while count <= target:
            node_aux = node_aux.next
            count += 1

        return node_aux.data


    def fastslow(self, n):
        fast =  slow = self.head

        count = 0

        while count < n:
            count +=1
            fast = fast.next

        while fast.next != None:
            fast = fast.next
            slow = slow.next

        return slow.data


    def printarinverso(self, node = None):
        if node == None:
            node = self.head

        if node.next != None:
            self.printarinverso(node.next)

        print(node.data)

    def insertInOrder(self, lista, data):
        if lista.length == 0:
            lista.insertBeginning(data)
        current = lista.head
        while current.next != None:
            if current.next.data > data:
                break
            current = current.next
        newNode = Node(data)
        if current.next == None:
            current.next = newNode
        else:
            newNode.next = current.next
            current.next = newNode
    #não move o ultimo dado da lista, ajeitar
    def move_node(self, lista, k):
        if lista.length == 1:
            return
        current = lista.head.next
        prev = lista.head
        while current:
            if current.data == k:
                prev.next = current.next
                current.next = lista.head
                lista.head = current
                current = prev.next
            prev = current
            if current!=None:
                current = current.next



    def isCircular(self, lista):
        slow = fast = lista.head
        count = 0
        while fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = slow.next
                count += 1
                while fast != slow:
                    count += 1
                    slow = slow.next
        return count
    #fast anda 2 e slow anda 1, quando fast chegar ao final, o slow vai estar no meio da lista
    def list_mid(self, lista):
        slow = fast =lista.head
        c = 0
        while fast.next != None:
            ...

    def invert(self, lista):
        if lista.length <= 1:
            return
        current =lista.head
        prev = None
        while current.next != None:
            next=current.next
            current.next=prev
            prev= current
            current=next
        current.next = prev
        lista.head = current

lista_encadeada = LinkedList()
# lista_encadeada.insertBeginning('1')
# lista_encadeada.insertBeginning('2')
# lista_encadeada.insertBeginning('3')
# lista_encadeada.insertBeginning('4')
lista_encadeada.insertEnd(2)
lista_encadeada.insertEnd(2)
lista_encadeada.insertEnd(3)
lista_encadeada.insertEnd(5)
lista_encadeada.insertEnd(5)
# lista_encadeada.insertInOrder(lista_encadeada, 2)
# lista_encadeada.insertPosisition(3,5)
lista_encadeada.move_node(lista_encadeada, 5)
lista_encadeada.printList()

# print(lista_encadeada.fullForce(5))
# print(lista_encadeada.fastslow(5))

# lista_encadeada.printarinverso()
