class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str:
            return 0
        number, flag = 0, 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+':
            str = str[1:]
        for c in str:
            if c >='0' and c <='9':
                number = 10 * number + ord(c) - ord('0')
            else:
                break
        number = number * flag
        if number > 2147483647:
            number = 2147483647
        elif number < -2147483648:
            number = -2147483648
        return number

'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            res = 0
        return res

'''
if __name__ == '__main__':
    S = Solution()
    a = S.myAtoi("-2147483649 with words")
    a = S.myAtoi("  ")
    print(a)