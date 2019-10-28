# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.res = []
        level = [root]
        # count == 0
        while level:
            self.res.append([i.val for i in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        for i in range(len(self.res)):
            if i % 2 == 1:
                self.res[i] = self.res[i][::-1]
        return self.res