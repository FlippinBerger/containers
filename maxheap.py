from math import floor
class MaxHeap:
    '''implementation of a max heap'''
    def __init__(self, l = []):
        self.__l = l
        self.__size = len(l)

    def empty(self):
        return True if self.__size == 0 else False

    def size(self):
        return self.__size

    def buildMaxHeap(self):
        for i in range self.size():
            index = floor(i / 2)
            maxHeapify(index)
    
    def maxHeapify(index):
        if index > self.size() - 1:
            return
        i2 = index * 2
        i3 = i2 + 1
        best = index
        if index > self.size() - 1: 
            return
        if self.__l[i2] > self.__l[index]:
            best = i2
        if i3 < self.size() and self.__l[i3] > self.__l[best]:
            best = i3
        if best != index:
            swap(best, index)
            maxHeapify(best)
        
    def swap(i1, i2):
        temp = self.__l[i1]
        self.__l[i1] = self.__l[i2]
        self.__l[i2] = temp

