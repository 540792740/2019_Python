class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a,2) + int(b,2)
        a = str(a)
        a = bin(int(a, 10))
        a = a[2:len(a)]
        return a

if __name__ == '__main__':
    S = Solution()
    a = S.addBinary("11", "11")
    print(a)
