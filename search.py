import queue

#Node class used as simple implementation of 
#depth first search and breadth first search
#holds value of the node and a list of neighboring nodes
class Node:
    def __init__(self, value):
        self.val = value
        self.neighbors = []


#Going to assume that the graph coming in is a just a list of Nodes for this
#algorithmic implementation

#also, the first 2 will be for just searching for a stop value and return the
#value, or False if it isn't found

def depthFirstSearch(start, stop):
    #set of nodes visited to prevent recursion when the stop node is never found
    visited = set()
    
    #use a stack for depth first search, init with start list
    stack = [start]

    while len(stack) > 0:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if node.val == stop:
            return node.val
        for neighbor in node.neighbors:
            if neighbor not in visited:
                stack.append(neighbor)
        return False

def breadthFirstSearch(start, stop):
    visited = set()

    queue = deque([start])
    
    while len(queue) > 0:
        node = queue.pop()

        if node in visited:
            continue
        visited.add(node)

        if node.val == stop:
            return node.val
        for neighbor in node.neighbors:
            if neighbor not in visited:
                queue.appendleft(neighbor)
        return False

