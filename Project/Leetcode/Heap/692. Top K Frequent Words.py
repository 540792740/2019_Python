import collections, heapq
def topKFrequent(words, k):
    count = collections.Counter(words)
    res = []
    count_index = sorted(set(count.values()))[::-1]
    for index in count_index:
        if len(res) >= k: break
        list_res = []
        for i in count:
            if count[i] == index:
                list_res.append(i)
        res.extend(sorted(list_res))
    return res[:k]

topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1)
topKFrequent(["aaa","aa","a"], 1)

# heap 99%
def topKFrequent2(words, k):
    # Init dic, save all frequency of words
    dic = {}
    for i in words:
        dic[i] = dic.get(i, 0) + 1

    # Init heapify heap
    heap = []
    heapq.heapify(heap)

    # Push all word in dict into heap
    for key in dic:
        heapq.heappush(heap, (-dic[key], key))
    print(heap)
    # Init res
    res = []
    for i in range(k):
        curr = heapq.heappop(heap)
        res.append(curr[1])
    return res

    # Sort res alphabetically
    # res.sort()
    # print(res)
    # newres = []
    # for word in res:
    #     newres.append(word[1])
    # return newres

print(topKFrequent2(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(topKFrequent2(["aaa","aa","a"], 1))