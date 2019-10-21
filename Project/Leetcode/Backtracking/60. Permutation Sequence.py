'''
Since n, there are n! number, we check (n - 1)!
        if the number of (n - 1)! < k, the value must between
        (n - 1)! to n!
e.g: getpermutation(4, 9)
1.
start in '1': there are 3!=6
start in '2': there are also 3! = 6
so 9 - 6 = 3, current = 1, means first number is 2
pop(nums[1])

2.
then [1,3,4]:
start in '1': there are 2! = 2
3 - 2 = 1, current = 1, means first number is num[1] = 3
pop(num[1]) --> 3

3.
[1,4]:
start in '1': there are 1!, only left 1
so pop(0) = 1

---> 231

'''

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
            print(k)
            res += str(nums[current])
            # print(current)
            nums.pop(current)
        res += str(nums[0])
        return res
    def factorial(self, n):
        a = 1
        for i in range(1, n + 1):
            a = a * i
        return a
    # time Limit Exceeded but Correct, Backtracking/ Recursive
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
    test = S.getPermutation(4,24)
    # test = S.getPermutation(9, 219601)
    # print(test)