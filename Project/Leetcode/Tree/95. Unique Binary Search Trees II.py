# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.dfs(1, n + 1)
    def dfs(self, start, end):
        if start == end: return None
        res = []
        for i in range(start, end):
            for l in self.dfs(start, i) or [None]:
                for r in self.dfs(i + 1, end) or [None]:
                    print(l, r)
                    node = TreeNode(i)
                    node.left, node.right = l, r
                    res.append(node)
        return res