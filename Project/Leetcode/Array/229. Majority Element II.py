'''
more than 1 / 3, which means there are most 2 number can be selected
so we can just choose 2 candidate
'''

class Solution:

    # 15% Slow
    def majorityElement(self, nums):
        n = len(nums)
        Frequency = n / 3
        dic = {}
        res= []
        for i in nums:
            if i in dic and dic[i]> Frequency and i not in res:
                res.append(i)
            elif i in dic and dic[i] <= Frequency and i not in res:
                dic[i] += 1
                if dic[i] > Frequency:
                    res.append(i)
            elif i not in dic:
                dic[i] = 1
                if dic[i] > Frequency:
                    res.append(i)
        return res

    def majorityElement1(self, nums):
        # 92% beat
        res = []
        for x in set(nums):
            t = nums.count(x)
            if (t > len(nums) // 3):
                res.append(x)
        return res

    # 93% Boyer-moore algorithm
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for i in nums:
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = i, 1
            elif count2 == 0:
                candidate2, count2 = i, 1

            else:
                count1, count2 = count1 - 1, count2 - 1
        return [x for x in (candidate1, candidate2) if nums.count(x) > len(nums) / 3]


if __name__ == '__main__':
    S = Solution()
    test = S.majorityElement1([3,2,3])
    test = S.majorityElement1([1,2])
    test = S.majorityElement1([1])
    test = S.majorityElement1([])
    print(test)