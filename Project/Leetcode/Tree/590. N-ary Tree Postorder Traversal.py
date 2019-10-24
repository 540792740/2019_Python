class Solution(boject):
    # 60%
    def postorder(self, root):
        self.res = []
        if root:
            self.dfs(root)
            self.res.append(root.val)
        return self.res

    def dfs(self, root):
        print(root.val)
        if root:
            for child in children:
                self.dfs(child)
                self.append(child.val)
    # 89%
    def postorder1(self, root):
        if not root: return None
        stack = [root]
        res = []
        while stack:
            cur = stack.pop()
            if cur.children:
                for child in cur.children:
                    stack.append(child)
            res.append(cur.val)
        return reversed(res)