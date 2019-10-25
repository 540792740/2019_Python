'''
0. check when root is None
1. Deep Search, when abs(left - right) > 1, return false


'''
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                print(root.val)
                return -1
            return 1 + max(left, right)
        return check(root) != -1

root = TreeNode(3)
left = root.left = TreeNode(9)
right = root.right = TreeNode(20)
right = right.left = TreeNode(15)
right = right.left = TreeNode(7)
'''
             3
            / \
           9   20
               /
              15
              /
             8 
'''

S = Solution()
a = S.isBalanced(root)
print(a)