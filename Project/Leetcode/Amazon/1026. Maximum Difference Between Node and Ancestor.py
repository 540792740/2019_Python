'''
DFS, queue

Question:
1.  Is this a binary tree? or root can have 3 or more leaves?
2.  The value can have a negative number right?
3.  I need to return the max absolute value of two connected node. right?

Solve:
1.  I think I should use DFS recursive, write a helper function to find highest, lowest
    value from root to depth.

2.  return max absolute value.



'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Complexity is O(n), traverse all node just one time.
# Space complexity O()
class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        def helper(node, low, high):
            if not node: return high - low
            high = max(high, node.val)
            low = min(low, node.val)
            return max(helper(node.left, low, high), helper(node.right, low, high))
        return helper(root, root.val, root.val)

    def maxAncestorDiff1(self, root):
        res = 0
        # stack : root, low, high
        stack = [[root, root.val, root.val]]
        while stack:
            node, low, high = stack.pop()
            low = min(node.val, low)
            high = max(node.val, high)
            res = max(abs(high - low), res)

            if node.left:  stack.append([node.left, low, high])
            if node.right: stack.append([node.right, low, high])
        return res