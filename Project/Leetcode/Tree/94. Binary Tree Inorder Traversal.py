# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 74% # recursively
    def inorderTraversal(self, root: TreeNode):
        if not root: return None
        self.res = []
        def helper(root):
            if not root: return None
            if root:
                helper(root.left)
                self.res.append(root.val)
                helper(root.right)
        helper(root)
        return self.res
    # iteratively
    def inorderTraversal1(self, root: TreeNode):
        if not root: return None
        res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right