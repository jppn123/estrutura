class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class stack:
    def __init__(self):
        self.head = None

    def len(self):
        curr = self.head
        value = 0
        while curr:
            value+=1
            curr = curr.next
        return value

    def printList(self):
        node_aux = self.head
        while node_aux != None:
            print(node_aux.data)
            node_aux = node_aux.next

    def push(self, data):
        node = Node(data)
        node_aux = self.head
        if self.len() == 0:
            self.head = node
            return
        while node_aux.next != None:
            node_aux = node_aux.next
        node_aux.next = node


    def pop(self):
        if self.len() == 0:
            return "list without data error"
        if self.len() == 1:
            data = self.head.data
            self.head = None
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    
    def peek(self):
        if self.len() == 0:
            return "list without data error"
        return self.head.data
            
    def isEmpty(self):
        if self.len() == 0:
            return True
        return False
    
    def mathOperationValidator(self, operation):
        op = list(operation)
        stack_op = stack()
        for x in range(len(op)):
            if op[x] in "([{":
                stack_op.push(op[x])
            if op[x] in ")]}":
                pop = stack_op.pop()
                if pop == "(" and op[x] != ")":
                    return False
                if pop == "[" and op[x] != "]":
                    return False
                if pop == "{" and op[x] != "}":
                    return False
        return True    
                      

lk = stack()
print()
print("peek:", lk.peek(), end="\n\n")
print("list is empty?", lk.isEmpty(), end="\n\n")
print("try to remove without data:", lk.pop(), end="\n\n")
print("list:")
lk.push(2)
lk.push(22)
lk.push(222)
lk.printList()
print()
print("removed head:",lk.pop(), end="\n\n")
print("list modified:")
lk.printList()

print("peek:", lk.peek(), end="\n\n")

print("list is empty?", lk.isEmpty(), end="\n\n")
print("removing data")
print(lk.pop())
print(lk.pop())
print(lk.pop())

print(lk.mathOperationValidator("(2+1) * (2*3)"))
# print(lk.mathOperationValidator("](2)"))
