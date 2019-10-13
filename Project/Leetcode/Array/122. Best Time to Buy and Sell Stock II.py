class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # Actually this two line is useless, since in for loot, if there is no value
        # Cannot enter for loop, just return 0

        profit = 0
        for index, value in enumerate(prices):
            if index == 0:
                continue
            if prices[index - 1] < value:
                profit += value - prices[index - 1]
        return profit

if __name__ == '__main__':
    S = Solution()
    a = S.maxProfit([1,2,3,1,5])
    print(a)
