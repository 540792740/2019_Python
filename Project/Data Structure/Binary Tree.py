# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
class Solution(object):
    def MidTraversal(self, root):
        '''
        :param root: TreeNode
        :return: List[int]
        '''
        ans = []
        def recurse(root):
            if root:
                recurse(root.left)
                ans.append(root.val)
                recurse(root.right)
        recurse(root)
        return ans

    def MidTraversal1(self, root):
        stack = []
        ans = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = cur.left
            else:
                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right