#HashMap that accepts both integers and strings as keys
class HashMap:
    def __init__(self):
        #initialize and empty list with size 64
        self.__space = 64
        self.__l = [None] * self.__space
        
    #simple hash function based on ascii values    
    def __hash(self, key):
        #cast all keys to be strings to perform the operation
        key = str(key)

        total = 0
        for c in key:
            total += ord(c)
        return total % self.__space
    
    def add(self, key, val):
        #hash the key to get the index
        index = self.__hash(key)
        
        #check to see if we're updating, or adding a new [k,v] 
        if self.__l[index] is [None]:
            self.__l[index] = [key, val]
            return
        length = len(self.__l[index])
        #go through and try to find the value to update
        for i in range(length):
            if self.__l[index][i][0] == key:
                self.__l[index][i] = [key, val]
                return
        #key doesn't exist, handle this new found collision by appending
        self.__l[index].append([key, val])
    
    #deletes a [k,v] from the map
    def remove(self, key):
        index = self.__hash(key)
        if self.__l[index] is None:
            return -1
        length = len(self.__l[index])
        for i in range(length):
            print self.__l[index][0]
            print length
            if length == 1 and self.__l[index][0] == key:
                del self.__l[index]
            elif self.__l[index][i][0] == key:
                del self.__l[index][i]
                return 0
        return -1

    #get the value for key
    def get(self, key):
        index = self.__hash(key)
        if self.__l[index] is None:
            return 'Key doesn\'t exist'
        length = len(self.__l[index])
        for i in range(length):
            if self.__l[index][i][0] == key:
                return self.__l[index][i][1]
        return 'Key doesn\'t exist'


    #method used to print out all of the spaces in the list that are occupied
    def printMap(self):
        for i in range(self.__space):
            if self.__l[i] is None:
                continue
            print 'index: {0}\nlists:{1}'.format(i, self.__l[i])

        

