class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxium = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] > height[right]:
                maxium = max(maxium, height[right] * (right - left))
                right -= 1
            else:
                maxium = max(maxium, height[left] * (right - left))
                left += 1
        print(maxium)
        return maxium
S = Solution()
S.maxArea([1,8,6,2,5,4,8,3,7])