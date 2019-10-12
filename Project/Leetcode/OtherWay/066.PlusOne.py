'''
Plus one:
    结尾是9，变0向前，最前加1
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ls = len(digits) - 1
        while ls >= -1:
            if  ls == -1:
                digits[ls] = 0
                digits.insert(0, 1)
                break
            if digits[ls] == 9:
                digits[ls] = 0
                ls -= 1
            else:
                digits[ls] = digits[ls] + 1
                break
        return digits


if __name__ == '__main__':
    S = Solution()
    a = S.plusOne([1,2,3])
    a = S.plusOne([1,2,3,9])
    a = S.plusOne([9,9,9])
    print(a)
