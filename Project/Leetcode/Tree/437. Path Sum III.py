# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        self.ans = 0
        def search(root, memo):
            self.ans += memo.count(sum)
            if root.left:
                search(root.left, [x + root.left.val for x in memo] + [root.left.val])
            if root.right:
                search(root.right, [x + root.right.val for x in memo] + [root.right.val])

        search(root,[root.val])
        return self.ans