# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Recursive
class Solution(object):
    def maxDepth(self, root):
        if not root: return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return max(left_max, right_max) + 1


    def maxDepth1(self, root):
        if not root: return 0
        self.res = 1
        self.dfs(root, 1)
        return self.res
    def dfs(self, root, count):
        if not root.left and not root.right:
            if count > self.res:
                self.res = count
                return
        if root.left:  self.dfs(root.left, count + 1)
        if root.right: self.dfs(root.right, count + 1)
        return

    def maxDepth2(self):
        if not root:  return 0
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right and not queue: return val
            if curr.left:  queue.append((curr.left, val + 1))
            if curr.right: queue.append((curr.right, val + 1))