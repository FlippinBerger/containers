class Queue:
    '''A basic FIFO container'''
    
    def __init__(self):
        self.__l = []
        self.__size = 0

    def size(self):
        return self.__size

    def empty(self):
        return True if self.__size == 0 else False

    def push(self, val):
        self.__size += 1
        self.__l.append(val)

    def pop(self):
        self.__size -= 1
        return self.__l.pop(0)

    def front(self):
        return self.__l[0]

    def back(self):
        return self.__l[-1]
