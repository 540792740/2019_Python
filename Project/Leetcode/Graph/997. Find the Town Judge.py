class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        graph = {i:[] for i in range(1, N + 1)}
        for t in trust:
            graph[t[0]].append(t[1])
        print(graph)
        for k in graph:
            print((k))
            # judge don't trust anybody, so len() == 0
            if len(graph[k]) == 0:
                judge = k

                for person in graph:
                    if person != judge and judge not in graph[person]:
                        return -1
                return judge
        return -1

if __name__ == '__main__':
    S = Solution()
    test = S.findJudge(3,[[1,3],[2,3],[3,1]])
    print(test)