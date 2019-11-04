class Solution:
    def twoSum(self, nums, target):

        # res is set, to avoid duplicate pair
        res = set()
        dic = {}

        # Two number sum on target
        for i in range(len(nums)):

            # Save on target value in dic
            if nums[i] not in dic:
                dic[target - nums[i]] = i

            # Save on target pair
            else:

                if nums[i] not in res :
                    res.add((nums[i], nums[dic[nums[i]]]))
        print(res)
        return len(res)

    def twoSum1(self, nums, target):

        res = {}
        out = set()

        for index, value in enumerate(nums):
            if target - value in res:
                out.add((value, target - value))
            else:
                res[value] = index
        print(out)
        return len(out)


if __name__ == '__main__':
    S = Solution()
    test = S.twoSum([1,1,2,45,46,46], 47)
    print(test)
    test = S.twoSum([1,5,1,5], 6)
    print(test)
    test = S.twoSum([1,1], 2)
    print(test)

    test = S.twoSum1([1, 1, 2, 45, 46, 46], 47)
    print(test)
    test = S.twoSum1([1, 5, 1, 5], 6)
    print(test)
    test = S.twoSum1([1, 1], 2)
    print(test)
