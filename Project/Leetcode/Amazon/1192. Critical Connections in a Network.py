from collections import defaultdict
import collections

class Solution(object):
    # Tarjan 89%
    def criticalConnections(self, n, connections):
        g = defaultdict(set)
        for i, j in connections:
            g[i].add(j)
            g[j].add(i)

        # Init Visited, dfn, low
        res = []
        low = [0] * n
        dfn = [0] * n
        parent = [-1] * n
        visited = [False] * n
        self.times = 0

        # Tarjan algorithm find strong connectivity
        def tarjan(root):
            self.times += 1
            low[root] = dfn[root] = self.times
            visited[root] = True

            for v in g[root]:
                if not visited[v]:
                    parent[v] = root
                    tarjan(v)
                    low[root] = min(low[root], low[v])

                    if low[v] > dfn[root]:
                        res.append([v, root])

                # reboot low[u] as the lowest number to u
                elif v != parent[root]:
                    low[root] = min(low[v], low[root])
            return

        # Traverse Node
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