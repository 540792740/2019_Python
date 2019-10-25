# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 97%
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root: return []
        self.sum_level = []
        self.count = []
        def helper(root, level):
            if not root: return
            else:
                if level > len(self.sum_level) - 1:
                        self.sum_level.append(root.val)
                        self.count.append(1)
                else:
                    self.sum_level[level] += root.val
                    self.count[level] += 1
                if root.left:
                    helper(root.left, level + 1)
                if root.right:
                    helper(root.right, level + 1)
        helper(root, 0)
        for i in range(len(self.sum_level)):
            self.sum_level[i] = self.sum_level[i] / self.count[i]
        return self.sum_level
