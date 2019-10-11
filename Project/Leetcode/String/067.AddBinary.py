class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >=0 or carry == 1:
            carry += int(a[i]) if i >= 0 else 0
            carry += int(b[j]) if j >= 0 else 0
            res = str(carry % 2) + res
            i, j, carry = i - 1, j - 1, carry / 2
        return res

# By myself, beat 90%
    def addBinary1(self, a, b):
        a = int(a,2) + int(b,2)
        a = str(a)
        a = bin(int(a, 10))
        a = a[2:len(a)]
        return a

if __name__ == '__main__':
    S = Solution()
    a = S.addBinary("11", "11")
    print(a)
