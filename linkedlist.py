class Node:
    def __init__(self, datum = None):
        self.val = datum
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    #returns the head node of the linked list
    def head(self):
        return self.__head
    
    #adds a new node to the end of the linked list
    def append(self, new_node):
        if self.__size == 0:
            self.__head = new_node
            self.__size = 1
        else:
            node = self.head()
            while node.next != None:
                node = node.next
            node.next = new_node
            self.__size += 1
    
    #inserts a node at a specific index of the linked list
    def insert(self, new_node, pos):
        if pos == 0:
            self.__head = new_node
            self.__size = 1
        else:
            node = self.head()
            for i in range(pos - 1):
                node = node.next
            current = node
            next_node = current.next
            current.next = new_node
            new_node.next = next_node
            self.__size += 1

    def at(self, pos):
        node = self.head()
        for i in range(pos):
            node = node.next
        return node

    def remove(self, pos):
        if pos == 0:
            self.__head = self.__head.next
            self.__size -= 1
        else:
            for i in range(pos - 1):
                node = node.next
            current = node
            current.next = current.next.next
            self.__size -= 1

    def clear(self):
        self.__head = None
        self.__size = 0
