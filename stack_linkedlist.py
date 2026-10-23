class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class Stack:
    def __init__(self):
        self.head=None
        self.size=0
    def push(self, val):
        node=Node(val)
        if self.head:
            node.next=self.head
        self.head=node
        self.size+=1
    def pop(self):
        if self.isEmpty():
            raise ValueError("empty stack")
        poped_node=self.head
        self.head=self.head.next
        self.size-=1
        return poped_node.data
    def peek(self):
        if self.isEmpty():
            raise ValueError("empty stack")
        return self.head.data
    
    def isEmpty(self):
        return self.size == 0
    def traverseAndPrint(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print()
    def stackSize(self):
        return self.size

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("LinkedList: ", end="")
myStack.traverseAndPrint()
print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())
print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
        
        

        
