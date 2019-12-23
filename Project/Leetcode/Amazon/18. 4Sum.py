def fourSum(self, nums, target):
    def findNsum(nums, target, N, path, results):
        if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return
        # N == 2, Two Pointer
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(path + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        # Recursively to N == 2
        else:
            for i in range(len(nums) - N + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    findNsum(nums[i + 1:], target - nums[i], N - 1, path + [nums[i]], results)

    results = []
    findNsum(sorted(nums), target, 4, [], results)
    return results