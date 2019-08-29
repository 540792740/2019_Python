class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = len(numbers)
        left = 0
        right = ls - 1

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1,right + 1]



if __name__ == '__main__':
    S = Solution()
    a = S.twoSum([2,6,9,11], 8)
    print(a)