class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [True] + [False] * length

        for i in range(length):
            for j in range(0, i + 1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[-1]
if __name__ == '__main__':
    S = Solution()
    a = S.wordBreak("a", ["a"])
    # a = S.wordBreak("catsandog", wordDict = ["cats", "og", "sand", "and", "cat"])
    print(a)