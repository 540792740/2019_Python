# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 72%
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right and root:
            return 1
        level = [root]
        count = -1
        self.level_num = []
        while level:
            count += 1
            temp  = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
            if len(level) != 0:
                self.level_num.append(len(level))
        return 2**count + self.level_num[-1] - 1