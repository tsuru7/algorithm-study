class BinarySearchTree:

    def __init__(self, key=None):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.balance = 0

    def search(self, target):
        node = self
        while node is not None:
            if node.key == target:
                return node
            if target < node.key:
                node = node.left
            else:
                node = node.right
        return None

    def search_left(self, target):
        node = self
        while node is not None:
            if target < node.key:
                node = node.left
            else:
                if node.right is None:
                    return node
                node = node.right
        return None

    def search_right(self, target):
        node = self
        while node is not None:
            if target < node.key:
                if node.left is None:
                    return node
                node = node.left
            else:
                node = node.right
        return None

    def smallest(self):
        node = self
        while node is not None:
            prev = node
            node = node.left
        return prev

    def largest(self):
        node = self
        while node is not None:
            prev = node
            node = node.right
        return prev

    def isLeaf(self):
        if self.left is None and self.right in None:
            return True
        else:
            return False

    def insert(self, newkey):
        node = self.search(newkey)
        if node is not None:
            return node 
        newnode = BinarySearchTree(newkey)
        while node is not None:
            par = node
            if newkey < node.key:
                node = node.left
            else:
                node = node.right
        if newkey < par.key:
            node.left = newnode
        else:
            node.right = newnode
        newnode.parent = node
        return
    
    def delete(self, target):
        node = self
        while node is not None:
            if node.key == target:
                break
            if target < node.key:
                node = node.left
            else:
                node = node.right
        else:
            return None
        if node.left is None and node.right is None:
            par = node.parent




if __name__ == '__main__':
    root = BinarySearchTree()
    root.insert(10)
    print(root.key)
