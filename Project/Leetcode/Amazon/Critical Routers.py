import collections
from collections import defaultdict

class Solution:
    def findCriticalRouters(self, n, connections):
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
if __name__ == '__main__':
    S = Solution()
    test = S.findCriticalRouters(7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]])
    print(test, 'Result should be ', [[6, 5], [5, 2], [4, 3]])
    test = S.findCriticalRouters(10, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]])
    print(test)

'''
Given an underected connected graph with n nodes labeled 1..n. A bridge (cut edge) is defined as an edge which, when removed, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). Equivalently, an edge is a bridge if and only if it is not contained in any cycle. The task is to find all bridges in the given graph. Output an empty list if there are no bridges.

Input:

n, an int representing the total number of nodes.
edges, a list of pairs of integers representing the nodes connected by an edge.
Example 1:

Input: n = 5, edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]

Output: [[1, 2], [4, 5]]
Explanation:
There are 2 bridges:
1. Between node 1 and 2
2. Between node 4 and 5
If we remove these edges, then the graph will be disconnected.
If we remove any of the remaining edges, the graph will remain connected.
Example 2:

Input: n = 6, edges = [，；[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]

Output: []
Explanation:
We can remove any edge, the graph will remain connected.
Example 3:

Input: n = 9, edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]

Output: [[3, 4], [3, 6], [4, 5]]
'''

