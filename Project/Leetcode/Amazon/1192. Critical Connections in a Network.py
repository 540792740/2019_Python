from collections import defaultdict
import collections

class Solution(object):
    # Tarjan 89%
    def criticalConnections(self, n, connections):

        n = n + 1
        # Save all connections in to a dictionary(set)
        g = defaultdict(set)
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)
        print(g)

        # Init res, visited, low, dfn
        res = []
        visited = [False] * n
        low = [0] * n
        dfn = [0] * n
        parent = [-1] * n
        self.times = 0

        # Init tarjan algorithm, find strong connectivity
        def tarjan(root):
            print(low, dfn)
            self.times += 1
            low[root] = dfn[root] = self.times
            visited[root] = True

            # Traverse all node connect with root
            for v in g[root]:

                # Not visited Node
                if visited[v] == False:
                    parent[v] = root
                    tarjan(v)
                    low[root] = min(low[root], low[v])

                    # This will be a strong connection if minpath is less than original.
                    if low[v] > dfn[root]:
                        print(low, dfn, v, root)
                        res.append([v, root])

                # If v is not comes from root
                elif v != parent[root]:
                    low[root] = min(low[root], low[v])

            return

        for root in range(n):
            if visited[root] == False: tarjan(root)
        return res
    # 2 DFS
    def criticalConnections1(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g = collections.defaultdict(list)

        # Save all path in to dic g
        for i, u in connections:
            g[u].append(i)
            g[i].append(u)
        print(g)
        N = len(connections)
        lev = [None] * N
        low = [None] * N

        def dfs(node, par, level):
            print(node,par,level)

            # Already visited
            if lev[node] is not None:
                return
            lev[node] = low[node] = level
            for i in g[node]:
                if not lev[i]:
                    dfs(i, node, level + 1)
            cur = min([level] + [low[i] for i in g[node] if i != par])
            low[node] = cur
            print(low,lev)

        dfs(0, None, 0)
        ans = []
        for i, u in connections:
            if low[i] > lev[u] or low[u] > lev[i]:
                ans.append([u, i])
        return ans

if __name__ == '__main__':
    S = Solution()
    # test = S.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3],[3,2]])
    test = S.criticalConnections(3, [[0,1],[1,2],[2,0],[1,3]])
    print(test)
    test = S.criticalConnections(9, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]])
    print(test)
    test = S.criticalConnections(6, [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]])
    print(test)
