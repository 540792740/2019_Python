class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ls = len(nums)
        if ls == 0:
            return [-1,-1]
        min = 0
        max = ls - 1

        if target == nums[min]:
            while max - 1 >= 0 and nums[max] != target:
                max -= 1
            return [min,max]
        elif target == nums[max]:
            while min + 1 <= max and nums[min] != target:
                min += 1
            return [min, max]
        else:
            while min <= max:
                pos = int((min + max) / 2)
                if nums[pos] > target:
                    max = pos - 1
                elif nums[pos] < target:
                    min = pos + 1

                else:
                    print(max)
                    print(min)
                    for i in range(min, max + 1):
                        print(i)
                        if nums[i] == target:
                            if min < i and nums[min] != nums[i]:
                                min = i
                            max = i
                    return [min, max]
                '''
                else:
                    min = pos
                    max = pos
                    while nums[min - 1] == target:
                        min -= 1
                    while nums[max + 1] == target:
                        max += 1
                    return [min, max]
                '''

            return [-1, -1]


if __name__ == '__main__':
    S = Solution()
    a = S.searchRange([5,7,7,8,8,10],7)
    print(a)
    # a = S.searchRange([1,4],4)
    # print(a)