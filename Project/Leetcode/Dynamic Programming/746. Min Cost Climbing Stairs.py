class Solution:
    def minCostClimbingStairs(self, cost):

        ls = len(cost)
        dp = [0] * (ls + 1)
        if ls == 1: return cost[0]
        if ls == 2: return min(cost[0], cost[1])

        i = 2
        while i < ls + 1:
            step[i] = min(step[i - 1] + cost[i - 1], step[i - 2] + cost[i - 2])
            i += 1
        return step[-1]