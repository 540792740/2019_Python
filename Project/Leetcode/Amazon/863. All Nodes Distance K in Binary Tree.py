class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        graph = {}
        def connect(parent, child):
            if parent and child:
                graph[parent.val] = graph.get(parent.val, []) + [child.val]
                graph[child.val] = graph.get(child.val, []) + [parent.val]
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)
        connect(None, root)
        if not graph: return []
        bfs = [target.val]
        visited = set(bfs)
        for i in range(K):
            temp = []
            for x in bfs:
                print(x)
                print(graph[x])
                for y in graph[x]:
                    if y not in visited:
                        temp.append(y)
            bfs = temp
            # bfs = [y for x in bfs for y in graph[x] if y not in seen]
            visited = visited | set(bfs)
        return bfs

if __name__ == '__main__':
    S = Solution()
    test = S.distanceK(TreeNode(1),TreeNode(1),3)