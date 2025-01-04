class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """
        Never restructure，所以繼續往下去找，直到最下面的位置
        """
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def delete(self, node, target):
        """
        如果沒有左或右，單純回傳另一邊
        如果有，要去右邊找最小的，把最小值換上來，接下來遞迴去找右邊最小，一個一個做 delete 去換掉
        """
        if not node:
            return node
        if target > node.value:
            node.right = self.delete(node.right, target)
        elif target < node.value:
            node.left = self.delete(node.left, target)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Find the minimum from the right subtree
            cur = node.right
            while cur.left:
                # the left node is the smallest
                cur = cur.left
            node.val = cur.val
            node.right = self.delete(node.right, node.val)
        return node


    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        else: return True

    def inorder_traversal(self):
        """
        左邊先走完，再走右邊，保證會按照數字由小到大 print
        """
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        """
        value -> left -> right
        """
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.reorder_traversal()

    def postorder_traversal(self):
        """
        left -> right -> value
        """
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)