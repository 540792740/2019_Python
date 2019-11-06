from collections import defaultdict
import collections

class Solution(object):
    # Tarjan 89%
    def criticalConnections(self, n, connections):
        adj = defaultdict(set)
        for i, j in connections:
            adj[i].add(j)
            adj[j].add(i)
        print(adj)

        # Init Visited, dfn, low
        visited = [False] * n
        dfn = [0] * n
        low = [0] * n
        self.time = 0
        parent = [-1] * n

        res = []

        # Tarjan algorithm find strong connectivity
        def tarjan(u):
            visited[u] = True
            self.time += 1
            dfn[u] = low[u] = self.time
            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    tarjan(v)
                    low[u] = min(low[u], low[v])

                    if low[v] > dfn[u]:
                        res.append([u,v])

                # reboot low[u] as the lowest number to u
                elif v != parent[u]:
                    low[u] = min(low[u], dfn[v])

            return

        for root in range(n):
            if not visited[root]:
                tarjan(root)
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
    test = S.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
    print(test)