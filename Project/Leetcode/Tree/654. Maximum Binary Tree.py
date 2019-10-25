# Definition for a binary tree node.
class TreeNode:
    def __init__ (self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums: return None
        _max = max(nums)
        max_pos = nums.index(_max)
        root = TreeNode(_max)
        root.left = self.constructMaximumBinaryTree(nums[:max_pos])
        root.right = self.constructMaximumBinaryTree(nums[max_pos + 1:])
        return root