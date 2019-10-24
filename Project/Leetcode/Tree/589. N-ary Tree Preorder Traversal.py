"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root:
            self.res.append(root.val)
            for child in root.children:
                self.dfs(child)