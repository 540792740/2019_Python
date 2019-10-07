'''
            1
           / \
          2   5
         / \   \
        3   4   6
0. Initial self.prev
1. to end of order root(6)
            6.right --> None
            6.left  -->None
            self.prev --> root(6)
2. to next end root(5)
            5.right -->self.prev(root(6))
            5.left  -->None
            self.prev --> root(5)
            .
            .
            .
3. Reach the aim
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
'''

'''