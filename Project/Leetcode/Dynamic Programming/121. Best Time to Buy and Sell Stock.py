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



if __name__ == "__main__":
    S = Solution()
    S.maxProfit([2,1,4])
    # S.maxProfit([1])
    # S.maxProfit([])
    # S.maxProfit([1,2,3])
