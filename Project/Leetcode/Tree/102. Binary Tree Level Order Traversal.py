# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        ans = []
        level = [root]
        while level:
            ans.append([i.val for i in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = []
            for leaf in temp:
                if leaf:
                    level.append(leaf)
        return ans