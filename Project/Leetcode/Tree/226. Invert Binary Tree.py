# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    # 73% beat by myself
    def invertTree(self, root):
        if not root: return root

        if root.left or root.right:
            if root.right:
                right = root.right
            else:
                right = None
            if root.left:
                left = root.left
            else:
                left = None

            root.right = left
            root.left = right
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

    # BFS, queue 40%
    def invertTree1(self, root):
        queue = collections.deque([(root)])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right =node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
            return root

        return

    #DFS Stack 99% beat
    def invertTree2(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root


        return

    # 93% good solution
    def invertTree3(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root