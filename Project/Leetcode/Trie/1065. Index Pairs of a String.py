class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for word in words:
            i = text.find(word)
            while i != -1:
                res.append((i, i + len(word) - 1))
                i = text.find(word, i + 1)
                print(text.find(word, i))
            res.sort()
            return[[i, j] for i, j in res]


if __name__ == '__main__':
    S = Solution()
    test = S.indexPairs("thestoryofleetcodeandme", ["story","fleet","leetcode"])
    print(test)
