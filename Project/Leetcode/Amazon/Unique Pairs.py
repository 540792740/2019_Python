class Solution:
    def twoSum(self, nums, target):
        # Init res and dict
        res = set()
        dict = {}

        # Save target - i into dict and if there is pair of target, add into res
        for i in nums:
            if i not in dict:
                dict[target - i] = i
            elif i in dict and (dict[i], i) not in res:
                res.add((dict[i], i))

        print(res)
        return len(res)


if __name__ == '__main__':
    S = Solution()
    test = S.twoSum([1,1,2,45,46,46], 47)
    print(test)
    test = S.twoSum([1,5,1,5], 6)
    print(test)
    test = S.twoSum([1,1], 2)
    print(test)
