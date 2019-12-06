# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        # if not root: return True
        def check(l, r):
            if not l and not r: return True
            if not l or not r: return False
            if l.val == r.val:
                return (check(l.left, r.right) and check(l.right, r.left)) or(check(l.left, r.left) and check(l.right, r.right))
        return check(root1, root2)

