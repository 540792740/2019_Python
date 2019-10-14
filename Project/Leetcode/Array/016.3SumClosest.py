class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])

        for i in range(len(nums) - 2):
            k = len(nums) - 1
            j = i + 1

            while j < k:
                close_sum = nums[i] + nums[j] + nums[k]

                if close_sum == target:
                    return close_sum

                if abs(close_sum - target) < abs(ans - target):
                    ans = close_sum

                if close_sum < target:
                    j += 1
                elif close_sum > target:
                    k -= 1
                else:
                    break
        return ans

    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = sum(nums[:3])

        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                close_sum = nums[i] + nums[j] + nums[k]
                if close_sum == target:
                    return target

                if abs(target - close_sum) < abs(ans - target):
                    ans = close_sum

                if close_sum > target:
                    k -= 1
                elif close_sum > target:
                    j += 1
                else:
                    break
        return ans


if __name__=='__main__':
    S = Solution()
    a = S.threeSumClosest([0,2,1,-3], 1)
    a = S.threeSumClosest1([0,2,1,-3], 1)
    print(a)