class Solution(object):
    def getPermutation(self, n, k):
        res = ''
        nums = [i for i in range(1, n + 1)]
        for i in range(n - 1, 0, -1):
            base = self.factorial(i)
            current = 0
            while k > base:
                k -= base
                current += 1
            res += str(nums[current])
            nums.pop(current)
        res += str(nums[0])
        return res
    def factorial(self, n):
        a = 1
        for i in range(1, n + 1):
            a = a * i
        return a
    # time Limit Exceeded but Correct
    def getPermutation1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = []
        num = []
        for i in range(1, n + 1):
            num.append(i)
        self.index = 0
        def helper(subset, n):
            if not n :
                if self.index == k - 1:
                    return self.res.append(subset)
                else:
                    self.index += 1
                    return
            else:
                for i in range(0, len(n)):
                    if not self.res:
                        helper(subset + str(n[i]), n[:i] + n[i + 1:])

        res = helper('', num)
        return self.res[0]

if __name__ == '__main__':
    S = Solution()
    # test = S.getPermutation(3,3)
    # test = S.getPermutation(4,9)
    test = S.getPermutation(9, 219601)
    print(test)
    # print(str(1))