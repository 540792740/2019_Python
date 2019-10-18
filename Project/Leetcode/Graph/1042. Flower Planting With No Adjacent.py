class Solution(object):
    def gardenNoAdj(self, N, paths):
        res = [0] * N
        graph = [[] for i in range(N)]
        # Save all path in graph
        for step in paths:
            graph[step[0] - 1].append(step[1] - 1)
            graph[step[1] - 1].append(step[0] - 1)
        print(graph)
        for i in range(N):
            neighbor_colors = []
            for neighbor in graph[i]:
                neighbor_colors.append(res[neighbor])
            print(neighbor_colors)
            for color in range(1,5):
                if color in neighbor_colors:
                    continue
                res[i] = color
                break
        return res

if __name__ == '__main__':
    S = Solution()
    test = S.gardenNoAdj(3, [[1,2],[2,3],[3,1]])
    print(test)