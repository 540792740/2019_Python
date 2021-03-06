class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]
        i = 0
        while True:
            for j in range(1 << i, 1 << (i + 1)):
                if j <= num:
                    '''
                    j == 1 --> dp[0] / (dp[1 - 1]) + 1
                    j == 2 --> dp[o] / (dp[2 - 2]) + 1
                    j == 4 --> dp[0] + 1
                    '''
                    dp.append(1 + dp[j - (1 << i)])
                else:
                    return dp
            i += 1
        return dp
    def countBits1(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0, 1]
        while len(dp) <= num:
            dp.extend(list(map(lambda x : x + 1, dp)))
        return dp[:num + 1]


if __name__ =='__main__':
    S = Solution()
    a = S.countBits(5)
    a = S.countBits1(5)
    print(a)