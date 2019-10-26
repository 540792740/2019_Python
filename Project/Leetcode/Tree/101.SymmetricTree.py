# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 98%
    def isSymmetric(self, root):
        if not root: return True
        def isSym(L, R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root.left, root.right)

    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = []
        if root:
            arr.append(root)
        while arr:
            vals = []
            for i in arr:
                if i:
                    vals.append(i.val)
                else:
                    vals.append(None)
            if list(reversed(vals)) != vals:
                return False
            else:
                temp = []
                for i in arr:
                    if i:
                        temp.append(i.left)
                        temp.append(i.right)
                arr = temp
        return True

if __name__ == '__main__':
    root = TreeNode(1)
    left = root.left = TreeNode(2)
    right = root.right = TreeNode(2)
    left.left = TreeNode(3)
    left.right = TreeNode(4)
    right.left = TreeNode(4)
    right.right = TreeNode(3)
    S = Solution()
    a = S.isSymmetric(root)
    print(a)
