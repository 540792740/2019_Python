# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Recursive
        if not root:
            return[]
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

    # DFS
    def rightSideView1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view =[]
        collect(root,0)
        return view