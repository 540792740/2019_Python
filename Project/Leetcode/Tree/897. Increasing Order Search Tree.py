# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        array = self.inOrder(root, [])
        root = cur = TreeNode(array[0])
        for i in range(1, len(array)):
            cur.tight = TreeNode(array[i])
            cur = cur.right
        return root

    def inOrder(self, root, res):
        if not root: return
        # Save all in to list
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
        return res