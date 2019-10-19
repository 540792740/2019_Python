import collections
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)
        return [self.dfs(x, y, graph, set()) for x, y in queries]

    def dfs(self, x, y, graph, visited):
        if x not in graph or y not in graph:
            return -1
        if x == y:
            return 1

        for n in graph[x]:
            if n in visited:
                continue
            visited.add(n)
            d = self.dfs(n, y, graph, visited)
            if d != -1:
                return graph[x][n] * d
        return -1

if __name__ == '__main__':
    S = Solution()
    test = S.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
    print(test)