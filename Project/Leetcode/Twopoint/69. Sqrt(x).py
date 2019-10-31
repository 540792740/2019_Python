class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        if x == 0: return 0
        if x == 1: return 1

        # if x sqrt == mid ** 2, mid is return int
        while l < r:
            mid = (l + r) // 2
            # important, <<< (mid + 1), less than
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                r = mid
            else:
                l = mid + 1
        return mid

    #98%
    def mySqrt1(self, x):
        return int(math.sqrt(x))

