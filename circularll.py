class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class CircularLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def size(self):
        return self.__size

    def empty(self):
        return True if self.__size == 0 else False
    
    def clear(self):
        

    def append(self, new_node):
        if self.empty():
            self.__head = new_node
            self.__tail = new_node
        elif self.size() == 1:
            self.__head.next = new_node
            self.__tail = new_node
            new_node.next = self.__head
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            new_node.next = self.__head
    
    def remove(self, value):
        if self.size() == 0:
            return -1
        prev = None
        node = self.__head
        for i in range(self.size()):
            if i != 0:
                node = node.next
            if node.val == value:
                if self.size() == 1:
                    del self.__head
                    del self.__tail
                    self.__size = 0
                else:
                    prev.next = node.next
                    self.__size -= 1
                    if node is self.__head:
                        self.__head = node.next
                    elif node is self.__tail:
                        self.__tail = prev
                return i
            prev = node

                    

                


