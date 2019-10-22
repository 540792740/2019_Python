class Solution(object):

    def countArrangement(self, N):
        self. visited = [False] * N
        self.count = 0
        self.N = N
        def helper(index):
            if index == 0:
                self.count += 1
                return
            for i in range(1, self.N + 1):
                if (index % i == 0 or i % index == 0) and self.visited[i - 1] == False:
                    self.visited[i - 1] = True
                    helper(index - 1)
                    self.visited[i - 1] = False
        helper(N)
        return self.count


    # 30%，not good enough
    def countArrangement1(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0
        def helper(N, pos, used):
            if pos > N:
                self.count += 1
                return

            for i in range(1, N + 1):
                if used[i] == 0 and (i % pos == 0 or pos % i == 0):
                    used[i] = 1
                    helper(N, pos + 1, used)
                    used[i] = 0
        used = [0] * (N + 1)
        helper(N, 1, used)
        return self.count

if __name__ == '__main__':
    S = Solution()
    test = S.countArrangement(4)
    print(test)