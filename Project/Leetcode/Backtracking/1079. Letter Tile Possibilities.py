class Solution(object):
    # 40% beats
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()
        def helper(subset, t):
            if subset:
                res.add(subset)
            for i in range(len(t)):
                helper(subset + t[i], t[:i] + t[i + 1:])
        helper('', tiles)
        return len(res)

if __name__ == '__main__':
    S = Solution()
    test = S.numTilePossibilities('AAB')
    print(test)
