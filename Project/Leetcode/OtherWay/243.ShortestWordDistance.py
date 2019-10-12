class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """

        i1 = -1
        i2 = -1
        minium = len(words) - 1
        for i, str in enumerate(words):
            if str == word1:
                i1 = i
                if i2 > -1:
                    minium = min(minium, abs(i1 - i2))
            if str == word2:
                i2 = i
                if i1 > -1:
                    minium = min(minium, abs(i1 - i2))
        return minium


S = Solution()
a = S.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding','practice')
print(a)
