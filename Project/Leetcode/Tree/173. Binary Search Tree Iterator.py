# Definition for a binary tree node.
# 100%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        temp_node = self.stack.pop()
        self.pushAll(temp_node.right)
        return temp_node.val

    def hasNext(self):
        return self.stack

