'''
0.  No elment
1.  First element of inoder array is the root,
    second element is left part root.
    Third element is right part root....
2.  Rebuild Tree
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root


if __name__ == '__main__':
    S = Solution()
    a = S.buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(a)
