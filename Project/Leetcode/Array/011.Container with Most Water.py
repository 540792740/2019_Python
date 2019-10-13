'''
Area = height * length
max(maxium, Area)
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxium = area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            l,r = height[left], height[right]
            if height[left] > height[right]:
                area = (right - left) * height[right]
                while height[right] <= r and right > left:
                    right -= 1
            else:
                area = (right - left) * height[left]
                while height[left] <= l and left < right:
                    left += 1
            # maxium = max(maxium, area) this line is slower
            if area > maxium:
                maxium = area
        return maxium

S = Solution()
a = S.maxArea([1,8,6,2,5,4,8,3,7])
print(a)