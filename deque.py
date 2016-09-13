class Deque:
    def __init__(self):
        self.__l = []
        self.__size = 0

    def size(self):
        return self.__size

    def empty(self):
        return True if self.__size == 0 else False
    
    def clear(self):
        self.__size = 0
        self.__l = []

    def at(self, index):
        return self.__l[index]

    def front(self):
        return self.__l[0]

    def back(self):
        return self.__l[-1]

    def push_back(self, val):
        self.__l.append(val)
        self.__size += 1

    def push_front(self, val):
        self.__l.insert(0, val)
        self.__size += 1

    def pop_back(self):
        if self.__size >= 1:
            self.__size -= 1
            return self.__l.pop()

    def pop_front(self):
        if self.__size >= 1:
            self.__size -= 1
            return self.__l.pop(0)

    def erase(self, pos):
        if self.__size > pos:
            self.__size -= 1
            self.__l.pop(pos)
    
    #erases a range of values
    def erase(self, start, end):
        if start >= 0 and self.__size > end:
            while start < end:
                self.__size -= 1
                self.__l.pop(start)
                start += 1




