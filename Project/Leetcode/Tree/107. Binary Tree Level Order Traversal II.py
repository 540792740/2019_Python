# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        self.res = []
        level = [root]
        while level:
            self.res.append(i.val for i in level)
            temp = []
            for node in level:
                temp.extend([node.left, node.right])

            level = [leaf for leaf in temp if leaf]
        print(self.res)
        return self.res[::-1]

