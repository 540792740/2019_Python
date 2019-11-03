from collections import defaultdict
import collections

class Solution(object):
    def criticalConnections(self, n, connections):
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
    test = S.criticalConnections(4, [[0,1],[1,2],[2,0],[1,3],[3,2]])
    print(test)