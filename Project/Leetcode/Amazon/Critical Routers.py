import collections


class Router:
    def __init__(self, val):
        self.val = val
        self.link = []
    def addLink(self, router):
        self.links.append(router)

class Solution:
    def findCriticalRouters(self, numRouters, numLinks, Links):
        if not numRouters: return []
        if numRouters == 1: return[0]

        routers = [Router(i) for i in range(numRouters)]
        res = []

        # for i, u in Links:
        #     # routers[i]
        #     print(i, u)
        #     print(routers)
        for link in Links:
            routers[link[0]].links.append(link[1])
            routers[link[1]].links.append(link[0])

        return

    def dfs(self, rootNode, removedOne):

        return

if __name__ == '__main__':
    S = Solution()
    test = S.findCriticalRouters(7, 7, [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]])
    print(test)