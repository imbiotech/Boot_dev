class BSTNode:
    def get_min(self):
        if self.val is None:
            return None
        node = self
        while node.left is not None:
            node = node.left
        return node.val

    def get_max(self):
        if self.val is None:
            return None
        node = self
        while node.right is not None:
            node = node.right
        return node.val

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
