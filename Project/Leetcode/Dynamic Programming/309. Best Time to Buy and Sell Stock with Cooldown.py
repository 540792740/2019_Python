class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if not prices: return 0
        cash = [0] * length
        hold = [0] * length
        hold[0] = - prices[0]
        for i in range(1, length):
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (cash[i - 2] if i >= 2 else 0) - prices[i])
            print(cash)
            print(hold)
        return cash[-1]

if __name__ == '__main__':
    S = Solution()
    a = S.maxProfit([2,1,2,3,0,2])
    print(a)
