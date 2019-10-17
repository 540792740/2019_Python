'''
DFS
0.
1.
2.

Time: O(m*n)
Space: O(1)
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False

        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right, t.right)


