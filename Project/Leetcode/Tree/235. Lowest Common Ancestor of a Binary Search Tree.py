# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 30% myself
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = []

        def helper(root, path, p, q):
            if len(self.res) == 2:
                return
            if root.val == p.val or root.val == q.val and root:
                self.res.append(path + [root.val])
            if root.left:
                helper(root.left, path + [root.val], p, q)
            if root.right:
                helper(root.right, path + [root.val], p, q)

        helper(root, [], p, q)
        ls = min(len(self.res[0]), len(self.res[1]))
        num_min = self.res[0][0]
        for i in range(ls):
            if self.res[0][i] == self.res[1][i]:
                num_min = self.res[0][i]
        return TreeNode(num_min)

    # 97%
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            print('ss')
            return None
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
            # if p.val < root.val and q.val < root.val:
        else:
            return self.lowestCommonAncestor(root.left, p, q)