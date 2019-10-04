'''
Recursion:
find mid num, add the treeNode
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        size = len(nums)
        if size == 0:
            return None
        if size == 1:
            return TreeNode(nums[0])
        size //= 2
        root = TreeNode(nums[size])
        root.left = self.sortedArrayToBST(nums[:size])
        root.right = self.sortedArrayToBST(nums[size+1:])
        return root