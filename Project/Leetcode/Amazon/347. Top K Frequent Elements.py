import heapq
from collections import Counter
import collections
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    res = []
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    sorted_list = sorted(dic.items(), key = lambda d: d[1], reverse = True)
    for element in sorted_list:
        res.append(element[0])
        if len(res) == k:
            return res
    return res

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #   Init dic, key is element, values is frequent
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        #   Sorted based on values
        max_heap = [(-val, key) for key, val in dic.items()]
        heapq.heapify(max_heap)
        #   Return Top K
        return [heapq.heappop(max_heap)[1] for _ in range(k)]


def topKFrequent2(nums, k):
    # print(list(zip(*collections.Counter(nums).most_common(k)))[0])
    return [c[0] for c in Counter(nums).most_common(k)]

if __name__ == '__main__':
    # print(topKFrequent([1,1,1,2,2,3], 2))
    print(topKFrequent1([1,1,1,2,2,3], 2))