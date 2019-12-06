'''
0. root == None
1. End Node return 1, None return 0
2. Find minimize Depth
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        if not root: return 0
        if not root.left and not root.right: return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not left: return r + 1
        if not right: return l + 1
        return min(l, r) + 1