class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        self.res = 0
        x_reverse = x
        def reverse(a):
            if a == 0:
                return
            temp = a % 10
            a = a // 10
            self.res = self.res * 10 + temp
            reverse(a)
        if x > 0:
            reverse(x_reverse)
        else:
            reverse(-x_reverse) == -x
        return self.res == x

if __name__ == '__main__':
    S = Solution()
    test = S.isPalindrome(1221)
    print(test)