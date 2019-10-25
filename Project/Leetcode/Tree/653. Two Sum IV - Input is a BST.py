# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 92% beat
    def findTarget(self, root, k):
        if not root: return False
        self.dic = set()
        self.flag = False
        def helper(root, target):
            if self.flag != False: return
            if not root: return
            else:
                if root.val in self.dic:
                    self.flag = True
                    return
                else: self.dic.add(target - root.val)
                if root.left:
                    helper(root.left, target)
                if root.right:
                    helper(root.right, target)
        helper(root, k)
        return self.flag
    # beat 92%, same
    def findTarget(self, root, k):
        dic = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val in dic:
                    return True
                else:
                    dic.add(k - node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return False