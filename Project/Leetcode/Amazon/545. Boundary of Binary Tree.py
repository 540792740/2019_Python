class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs_leftmost(root):
            # when Leaf node, return
            if not root or not root.left and not node.right: return
            res.append(root.val)
            if root.left:
                dfs_leftmost(root.left)
            else:
                dfs_leftmost(root.right)

        def dfs_leaves(node):
            if not root: return

            # traverse to most left node
            dfs_leaves(node.left)

            # Add to res when no left node
            if node != root and not node.left and not node.right:
                res.append(node.val)
            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right: return
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)
            res.append(node.val)


        if not root: return []
        res = [root.val]
        dfs_leftmost(root.left)
        dfs_leaves(root)
        dfs_rightmost(root.right)
        return res

if __name__ == '__main__':
    S = Solution()
    test = S.boundaryOfBinaryTree([1,null,2,3,4])
    print(test)