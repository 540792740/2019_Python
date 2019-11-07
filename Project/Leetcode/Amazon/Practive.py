import collections

class Solution:
    def TwoSum(self, nums, target):
        # Init res and dict
        res = set()
        dict = {}

        # Save target - i into dict and if there is pair of target, add into res
        for i in nums:
            if i not in dict:
                dict[target - i] = i
            elif i in dict and (dict[i], i) not in res:
                res.add((dict[i], i))

        print(dict)
        return len(res)




        return
if __name__ == '__main__':
    S = Solution()
    test = S.TwoSum([1, 1, 2, 45, 46, 46], 47)
    print(test)
    test = S.TwoSum([1, 1], 2)
    print(test)
    test = S.TwoSum([1, 5, 1, 5], 6)
    print(test)