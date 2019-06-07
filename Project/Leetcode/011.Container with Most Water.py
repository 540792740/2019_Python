class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxium = 0
        a = 0
        b = len(height) - 1
        while a < b:
            if height[a] <= height[b]:
                maxium = max(maxium, (b -a) * height[a])
                a += 1
            else:
                maxium = max(maxium, (b - a) * height[b])
                b -= 1
        return maxium

S = Solution()
S.maxArea([1,8,6,2,5,4,8,3,7])