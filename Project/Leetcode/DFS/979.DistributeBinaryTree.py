# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = 0
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left + right - 1
        dfs(root)
        return self.res