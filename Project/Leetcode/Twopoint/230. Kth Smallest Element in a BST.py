# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        # 100%
        stack = [root]
        while stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            else:
                root = root.right


    # 62% Recursive
    def kthSmallest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.res = None

        def helper(root):
            if not root or self.count == 0: return
            helper(root.left)
            self.count -= 1
            if self.count == 0:
                 self.res = root.val
                 return
            self.helper(root.right)
        helper(root)
        return self.res