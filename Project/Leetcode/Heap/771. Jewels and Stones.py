class Solution(object):

    def numJewelsInStones(self, J, S):
        print(map(J.count, S))


    def numJewelsInStones1(self, J, S):
        return sum(i in J for i in S)

    # 77%
    def numJewelsInStones2(self, J, S):
        count = 0
        for i in S:
            if i in J: count += 1
        return count

if __name__ == '__main__':
    S = Solution()
    test = S.numJewelsInStones("aA", "aAAbbbb")