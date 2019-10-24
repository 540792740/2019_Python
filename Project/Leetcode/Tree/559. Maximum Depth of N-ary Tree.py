"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

# 90%
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        self.max_depth = 1

        def dfs(root, count):
            if count > self.max_depth:
                self.max_depth = count
            if root.children:
                for child in root.children:
                    dfs(child, count + 1)

        dfs(root, 1)
        return self.max_depth