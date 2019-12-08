# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 95% beat, recursion
    def findTarget(self, root, k):
        if not root: return False
        dic = set()

        def find(root):
            if not root: return False
            if root.val in dic:
                return True
            else:
                dic.add(k - root.val)
            left = find(root.left)
            right = find(root.right)
            return left or right
        return find(root)


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