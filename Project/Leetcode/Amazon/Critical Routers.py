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
import collections
def findCriticalRouters(n, connections):

    # Save all connections into a dic() g
    g = collections.defaultdict(set)
    for i, j in connections:
        g[i].add(j)
        g[j].add(i)

        # Init visited, low, dfn
    visited = [False] * n
    low = [0] * n
    dfn = [0] * n
    global times
    times= 0
    parent = [-1] * n
    res = []

    # Tarjan algorithm
    def tarjan(root):
         # value times, visited, low and dfn
        times += 1
        visited[root] = True
        low[root] = times
        dfn[root] = times

            # Traverse connection with root
        for i in g[root]:
            if visited[i] == False:
                parent[i] = root
                tarjan(i)

                # return a min path of root when root connect to i.
                low[root] = min(low[root], low[i])

                # Append res when connection between root and is a strong connection
                if low[i] > dfn[root]:
                    res.append([i, root])


            # find min path when i and root not connect
            elif i != parent[root]:
                low[root] = min(low[root], low[i])
        return
    # Traverse all root in g
    for root in g:
        if not visited[root]:
            tarjan(root)

    return res
findCriticalRouters(7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]])
#
# if __name__ == '__main__':
#     S = Solution()
#     test = S.findCriticalRouters(7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]])
#     print(test, 'Result should be ', [[6, 5], [5, 2], [4, 3]])
#     test = S.findCriticalRouters(10, [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]])
#     print(test)
'''
def a():
    times = 0
    def b():
        nonlocal times
        times += 1
    b()
    print(times)
    return times
a()