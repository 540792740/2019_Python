import collections
def possibleBipartition(N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        color = [0] * (N + 1)
        print(graph)

        for i in range(1, N + 1):
            if color[i] != 0: continue
            bfs = collections.deque()
            bfs.append(i)
            color[i] = 1
            while bfs:
                print(color)
                cur = bfs.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        bfs.append(e)
        return True


print(possibleBipartition(4, [[1,2],[1,3],[2,4]]))

