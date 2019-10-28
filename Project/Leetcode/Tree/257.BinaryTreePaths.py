# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 97%
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return None
        self.res = []

        def helper(root, path):
            if not root: return None
            if root:
                print(root.val)
                if not root.left and not root.right:
                    self.res.append(path)
                if root.left:
                    helper(root.left, path + '->' + str(root.left.val))
                if root.right:
                    helper(root.right, path + '->' + str(root.right.val))

        helper(root, str(root.val))
        return self.res


    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        stack = [(root,'')]
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, ls + str(node.val) + '->'))

            return res
