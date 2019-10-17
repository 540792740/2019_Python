'''
DFS
0.
1.
2.

Time: O(m*n)
Space: O(1)
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        string_s = self.traverse_tree(s)
        string_t = self.traverse_tree(t)
        if string_t in string_s:
            return True
        return False

    def traverse_tree(self, s):
        if s:
            print(f"{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}")
            return f"d{s.val} {self.traverse_tree(s.left)} {self.traverse_tree(s.right)}"
        return None

class Solution1(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t:
            return True
        if not s or not t:
            return False

        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isSameTree(s.left,t.left) and self.isSameTree(s.right, t.right)


if __name__ == '__main__':
    S = Solution()
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.left.right = TreeNode(2)
    t = TreeNode(4)
    t.left = TreeNode(1)
    t.right = TreeNode(2)
    a = S.isSubtree(s,t)
    print(a)


