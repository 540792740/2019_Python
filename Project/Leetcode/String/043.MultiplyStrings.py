
class Solution:
    # 20%, it is a way to the solution
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == 0:
            return '0'
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                first, second = multi //10, nulti % 10
                curr += (second + pre) * (10 ** j)
                pre = first
            curr += pre * (10 **len(num1))
            ans +=  curr * (10 ** i)
        return str(ans)


    # Cannot test this. LOL
    def multiply1(self, num1, num2):
        return str(int(num1) + int(num2))


if __name__ == '__main__':
    S = Solution()
    a = S.multiply()
    print(a)