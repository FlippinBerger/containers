class Node:
    def __init__(self):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, root = None):
        self.root = root
        self.__size = 0 if root is None else 1

    def empty(self):
        return True if self.root is None else False

    def size(self):
        return self.__size

    def insert(self, node, data):
        if node is None:
            return Node(data)
        #if data is smaller than the parent go left
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        return node

    def search(self, node, data):
        '''searches the tree for a node with data'''
        #returns a None if data is not found, or the proper node
        if node is None or node.data == data:
            return node
        if node.data < data:
            return search(node.right, data)
        else:
            return search(node.left, data)

    def delete(self, node, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else: #we have the node to delete
            if self.isLeaf(node):
                del node
                self.__size -= 1
                return
            if node.left is None:
                new = node.right
                del node
                return new
            elif node.right is None:
                new = node.left
                del node
                return new
            else: #we are at the case where the node has children that need a home
                if node.data < root.data:
                    self.moveSmallSubTree(node.left, node.right)
                    return node.right
                else:
                    self.moveLargeSubTree(node.left, node.right)
                    return node.left


    #boolean check to see if a node is a leaf
    def isLeaf(self, node):
        return True if node.left is None and node.right is None else False

    #method to move a lesser valued subtree to the left side of the smallest
    #value in the right subtree when deleting a node with a left and right side
    def moveSmallSubTree(self, left, right):
        while right.left:
            right = right.left
        right.left = left

    def moveLargeSubTree(self, left, right):
        while left.right:
            left = left.right
        left.right = right

    def preOrderTraversal(self, node):
        print node.data
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

    def inOrderTraversal(self, node):
        inOrderTraversal(node.left)
        print node.data
        inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print node.data

