# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum1(self, root: TreeNode, sum: int) -> int:
        if not root: return 0
        self.ans = 0
        def search(root, memo):
            self.ans += memo.count(sum)
            if root.left:
                search(root.left, [x + root.left.val for x in memo] + [root.left.val])
            if root.right:
                search(root.right, [x + root.right.val for x in memo] + [root.right.val])

        search(root,[root.val])
        return self.ans

    # N^2
    def pathSum2(self, root: TreeNode, sum: int) -> int:
        self.numOfPaths = 0
        def test(node, target):
            if node is Node: return
            if node.val == target:
                self.numOfPaths += 1

                # Test break down
            test(node.left, target - node.val)
            test(node.right, target - node.val)


        def dfs(node, target):
            if node is Node: return

            test(node, target)
            dfs(node.left, target)
            dfs(node.right, target)

        dfs(root, target)
        return self.numOfPaths

    def pathSum2(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        cache = {0 : 1}

        def dfs(node, target, curPathSum, cache):
            if not node: return

            curPathSum += node.val
            oldPathSum = curPathSum - target

            self.res += cache.get(oldPathSum, 0)
            cache[curPathSum] = cache.get(curPathSum, 0) + 1

            dfs(node.left, target, curPathSum, cache)
            dfs(node.right, target, curPathSum, cache)

            cache[curPathSum] -= 1

        dfs(root, sum, 0, cache)
        return self.res