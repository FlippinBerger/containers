class Stack:
    '''An implementation of a stack in Pyhton'''
    def __init__(self):
        self.__l = []
        self.__size = 0

    def push(self, val):
        self.__l.append(val)
        self.__size += 1

    def pop(self):
        self.__size -= 1
        return self.__l.pop(-1)

    def size(self):
        return self.__size

    def empty(self):
        return True if self.__size == 0 else False
    
    def top(self):
        if self.__size > 0:
            return self.__l[-1]
        else:
        #fix this eventually to throw an error
            return 0
