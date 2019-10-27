class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        self.depth(root)
        return self.res
    def depth(self, root):
        if not root: return 0
        l = self.depth(root.left)
        r = self.depth(root.right)
        self.res = max(self.res, l + r)
        return max(l, r) + 1