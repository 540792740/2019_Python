# 100% beat

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = []

        def helper(root, path):
            if not root.left and not root.right:
                self.res.append(path)
                return
            if root:
                if root.left:
                    helper(root.left, path + str(root.left.val))
                if root.right:
                    helper(root.right, path + str(root.right.val))

        helper(root, str(root.val))
        summary = 0
        for i in self.res:
            summary += int(i, 2)
        return summary

a = '10'
print(bin(int(a)))