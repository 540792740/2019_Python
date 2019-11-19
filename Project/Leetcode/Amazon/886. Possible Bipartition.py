import collections
def possibleBipartition(N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Init Graph, add all list into grapg
        dic = collections.defaultdict(list)
        for i, j in dislikes:
            dic[i].append(j)
            dic[j].append(i)

        # Init color, a list save N + 1 elements
        color = [0] * (N + 1)

        # Add all graph into color
        for i in range(1, N + 1):
            if color[i] != 0: continue
            bfs = [i]
            color[i] = 1
            while bfs:
                cur = bfs.pop()
                for e in dic[cur]:
                    if color[e] == 0:
                        color[e] = -color[cur]
                        bfs.append(e)
                    else:
                        if color[cur] == color[e]:
                            return False
        return True


print(possibleBipartition(4, [[1,2],[1,3],[2,4]]))

