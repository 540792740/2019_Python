'''
Don't forgot 《and count < length》 in while loop
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows <= 1):
            return s
        arr = [''] * numRows
        length = len(s)
        count = 0
        inc = 0
        while count < length:
            if inc == 0:
                while inc < numRows and count < length:
                    arr[inc] += s[count]
                    inc += 1
                    count += 1

            elif inc == numRows:
                inc -= 2
                while inc > 0 and count < length:
                    arr[inc] += s[count]
                    count += 1
                    inc -= 1

        return ''.join(arr)


if __name__ == '__main__':
    S = Solution()
    a = S.convert("PAYPALISHIRING", 3)
    print(a)