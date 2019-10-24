# 99.73%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1 = []
        list2 = []

        def helper(root, list):

            if not root.left and not root.right:
                list.append(root.val)
            if root:
                if root.left:
                    helper(root.left, list)
                if root.right:
                    helper(root.right, list)

        helper(root1, list1)
        helper(root2, list2)
        if list1 == list2:
            return True
        else:
            return False