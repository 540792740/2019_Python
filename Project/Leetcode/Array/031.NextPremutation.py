'''
下一个字典序，先交换，然后reverse。
Example: 1,2,3,5,4,2
         1,2,3,2,4,5
         1,2,4,2,3,5
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        self.reverse(nums, i, n - 1)

        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    self.swap(nums, i - 1, j)
                    break
        return nums
    def reverse(self, nums, i, j):
        """
        contains i and j.
        """
        # for k in range(i, int((i + j) / 2 + 1)):
        #     self.swap(nums, k, i + j - k)
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        """
        contains i and j.
        """
        nums[i], nums[j] = nums[j], nums[i]




if __name__ == '__main__':
    s = Solution()
    # s.nextPermutation([1,5,8,4,7,6,5,3,1])
    a = s.nextPermutation([1,2,3])
    # s.nextPermutation([2,3,1])
    # s.nextPermutation([5,1,1])
    print(a)
