'''
Good question
'''

class Solution(object):
    def moveZeroes(self, nums):
        ls = len(nums)
        non_zero = 0
        for i in range(ls):
            if nums[i] != 0:
                nums[non_zero], nums[i] = nums[i], nums[non_zero]
                non_zero += 1
                print(nums)
        return nums
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        left = right = 0
        while right < ls:
            if left == right == 0:
                nums.append(0)
                left += 1
                right += 1
            if nums[right] == 0:
                nums[left + 1 : right + 1] = nums[left : right ]
                left += 1
                nums.append(0)
            right += 1
        return nums[left:]


if __name__ == '__main__':
    S= Solution()
    a = S.moveZeroes([0,1,1,1,1,0,3,12])
    a = S.moveZeroes([0,1,0,3,12])
    print(a)
