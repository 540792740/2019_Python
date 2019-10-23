# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    # 97% Good Solution
    def rangeSumBST(self, root, L, R):
        self.summary = 0
        def helper(root, L, R):
            if root:
                if L <= root.val <= R:
                    self.summary += root.val
                if root.val > L:
                    helper(root.left, L, R)
                if root.val < R:
                    helper(root.right, L, R)
        helper(root, L, R)
        return self.summary

    # 40%
    def rangeSumBST1(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.summary = 0
        def helper(root, L, R):
            if L <= root.val <= R:
                self.summary += root.val
            if not root.left and not root.right:
                return
            if root.left:
                helper(root.left, L, R)
            if root.right:
                helper(root.right, L, R)
        helper(root, L, R)
        return self.summary
