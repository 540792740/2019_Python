# Trash Code use brust-force, beat 6.7%

# DP
'''
0.  Generate two dp arrays of max profit, min price.
1.  Dynamic process loop from 1 to end, max profit is price - minimum price
    min_price i min_price.
2.  In two arrays, compare and get the max profit and min price
3.  Return profit
'''
class Solution(object):
    def maxProfit(self, prices):
        ls = len(prices)
        if ls == 0:
            return []
        prices = prices[::-1]
        high_price = prices[0]
        max_profit = 0
        for price in prices:
            if price > high_price:
                high_price = price
            if high_price - price > max_profit:
                max_profit = high_price - price
        return max_profit


    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length == 0:
            return 0
        max_profit = [0] * length
        min_price = [0] * length
        min_price[0] = prices[0]
        for i in range(1, length):
            max_profit[i] = max(prices[i] - min_price[i - 1], max_profit[i -1])
            min_price[i] = min(prices[i], min_price[i - 1])
        return max_profit[length - 1]



if __name__ == "__main__":
    S = Solution()
    a = S.maxProfit([2,3,4,1,6])
    # S.maxProfit([1])
    S.maxProfit([])
    # S.maxProfit([1,2,3])
    print(a)



'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices) - 1
        if length < 1:
            return 0
        return self.divide(prices, 0, length)

    def divide(self, prices, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2

        lmin = prices[left]
        for i in range(left, mid + 1):
            if prices[i] < lmin:
                lmin = prices[i]
        rmax = prices[right]

        for i in range(mid + 1, right + 1):
            if prices[i] > rmax:
                rmax = prices[i]
        maxlength = rmax - lmin

        l_maxlength = self.divide(prices, left, mid)
        r_maxlength = self.divide(prices, mid + 1, right)

        if l_maxlength > maxlength:
            maxlength = l_maxlength
        if r_maxlength > maxlength:
            maxlength = r_maxlength
        print(maxlength)
        return maxlength
'''
