'''
if not revers, use digits.insert(0,1)
s
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = False
        digits = digits[::-1]
        for i in range(len(digits)):
            if digits[i] == 9:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
                    return digits[::-1]
                continue
            else:
                digits[i] += 1
                break

        return digits[::-1]

if __name__ == '__main__':
    S = Solution()
    a = S.plusOne([1,2,3])
    print(a)
