class Node:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None
    
    def clear(self):
        self.__size = 0
        self.__head = None
        self.__tail = None
    
    def size(self):
        return self.__size

    def head(self):
        return self.__head

    def tail(self):
        return self.__tail

    def append(self, new_node):
        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node
            self.__size = 1
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
            self.__size += 1

    def insert(self, new_node, pos):
        if pos < 0 or pos >= self.size + 1
            return
        if pos == 0:
            new_node.prev = None
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        elif pos == self.size:
            new_node.prev = self._tail
            new_node.next = None
            self.__tail.next = new_node
            self.__tail = new_node
        else:
            current = self.__head
            for i in range(pos - 1):
                current = current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
        self.__size += 1

    def remove(self, pos):
        if pos < 0 or pos >= self.size:
            return
        if pos == 0:
            self.__head = self.__head.next
            self.__head.prev = None
        elif pos == self.__size - 1:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            victim = self.__head
            for i range(pos):
                victim = victim.next
            victim.prev.next = victim.next
            victim.next.prev = victim.prev
        self.__size -= 1
