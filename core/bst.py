"""
Binary Search Tree - Core Logic
"""


class Node:
    """A node in the BST"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.x = 0  # For GUI positioning
        self.y = 0


class BST:
    """Binary Search Tree"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value"""
        if not self.root:
            self.root = Node(value)
            return self.root
        return self._insert(self.root, value)

    def _insert(self, node, value):
        if value == node.value:
            return None  # Duplicate
        if value < node.value:
            if node.left:
                return self._insert(node.left, value)
            node.left = Node(value)
            return node.left
        else:
            if node.right:
                return self._insert(node.right, value)
            node.right = Node(value)
            return node.right

    def search(self, value):
        """Search for a value"""
        return self._search(self.root, value)

    def _search(self, node, value):
        if not node:
            return None
        if value == node.value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    def delete(self, value):
        """Delete a value"""
        self.root, deleted = self._delete(self.root, value)
        return deleted

    def _delete(self, node, value):
        if not node:
            return None, None
        
        if value < node.value:
            node.left, deleted = self._delete(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete(node.right, value)
            return node, deleted
        else:
            # Found it
            if not node.left and not node.right:
                return None, node
            if not node.left:
                return node.right, node
            if not node.right:
                return node.left, node
            
            # Two children - find successor
            succ = node.right
            while succ.left:
                succ = succ.left
            node.value = succ.value
            node.right, _ = self._delete(node.right, succ.value)
            return node, node

    def inorder(self):
        """Get nodes in order"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node)
            self._inorder(node.right, result)

    def preorder(self):
        """Get nodes preorder"""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """Get nodes postorder"""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node)