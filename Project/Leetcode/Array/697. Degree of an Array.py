class Solution:
    def findShortestSubArray(self, nums):
        indices_dic = {}
        for i, n in enumerate(nums):
            if n in indices_dic:
                indices_dic[n].append(i)
            else:
                indices_dic[n] = [i]
            # print(indices_dic)
        M = max([len(i) for i in indices_dic.values()])
        return min([i[-1] - i [0] for i in indices_dic.values() if len(i) == M]) + 1
    # 45%
    def findShortestSubArray(self, nums):
        if not nums: return 0
        dic = {}
        dic_distance = {}
        count = 1
        length = 1
        #       find the number which can show most times
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
                if count < dic[nums[i]]:
                    count = dic[nums[i]]
                    length = i - dic_distance[nums[i]] + 1

                if count == dic[nums[i]]:
                    if i - dic_distance[nums[i]] < length:
                        length = i - dic_distance[nums[i]] + 1
            else:
                dic[nums[i]] = 1
                dic_distance[nums[i]] = i
        return length