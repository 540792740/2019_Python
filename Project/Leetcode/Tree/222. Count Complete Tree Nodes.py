# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 还没来得及看
    def getHeight(self, root):
        height = 0
        while root:
            height += 1
            root = root.left
        return height

    def countNodes(self, root):
        count = 0
        while root:
            l, r = map(self.getHeight, (root.left, root.right))
            if l == r:
                count += 2 ** l
                root = root.right
            else:
                count += 2 ** r
                root = root.left
        return count


    # 72% myself
    def countNodes1(self, root: TreeNode) -> int:
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