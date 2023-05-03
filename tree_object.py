## Structure of the tree.

class BinaryTree:

    def __init__(self, data=None, left=None, right=None):
        """Create a binary tree."""
        self.data = data
        self.left = left
        self.right = right

    def getLeft(self):
        """Return the left child of the node."""
        return self.left

    def getRight(self):
        """Return the right child of the node."""
        return self.right

    def getData(self):
        """Return the data of the node."""
        return self.data

    def setLeft(self, left):
        """Set the left child of the node, which must be a BinaryTree type object."""
        if type(left) is BinaryTree:
            self.left = left

    def setRight(self, right):
        """Set the right child of the node, which must be a BinaryTree type object."""
        if type(right) is BinaryTree:
            self.right = right

    def setData(self, data):
        """Set the data of the node, which can not be a BinaryTree type object."""
        if type(data) is not BinaryTree:
            self.data = data

    def size(self):
        """Return the size of the binary tree, so the number of nodes if this method is applied to the root of the tree."""
        if self.left is None and self.right is None:
            return 1
        elif self.left is not None and self.right is None:
            return 1+self.left.size()
        elif self.left is None and self.right is not None:
            return 1+self.right.size()
        else:
            return 1+self.left.size()+self.right.size()

    def __len__(self):
        """Return the result of the binary tree, so the result of self.size(). You should consider using self.size() to avoid confusions when using this method."""
        return self.size()