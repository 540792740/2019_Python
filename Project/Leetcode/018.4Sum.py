class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        resultList = []
        nums.sort()
        for num1 in range(0, len(nums)-3):
            for num2 in range(num1 + 1, len(nums)-2):
                num3 = num2 + 1
                num4 = len(nums) -1
                while num3 != num4:
                    summer = nums[num1] + nums[num2] + nums[num3] + nums[num4]
                    if summer == target:
                        list_temp = [nums[num1],nums[num2],nums[num3],nums[num4]]
                        if list_temp not in resultList:
                            resultList.append(list_temp)
                        num3 += 1
                    elif summer > target:
                        num4 -= 1
                    else:
                        num3 += 1
        return resultList

# Hash table:
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        numLen, res, num_dict = len(nums), set(), {}
        if numLen < 4:
            return []
        nums.sort()
        for p in range(numLen):  # 存储hash表
            for q in range(p+1, numLen):
                if nums[p]+nums[q] not in num_dict:
                    num_dict[nums[p]+nums[q]] = [(p,q)]
                else:
                    num_dict[nums[p]+nums[q]].append((p,q))
                # print num_dict
        for i in range(numLen):
            for j in range(i+1, numLen-2):
                T = target-nums[i]-nums[j]
                if T in num_dict:
                    for k in num_dict[T]:
                        if k[0] > j: res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res]
