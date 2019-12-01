'''
I think i should use two pointer to solve the problem.
I will init l, r
at the same time ,I need another two point to record the maxium l and maxium r
keep replace this four pointer to solve
'''

# O(n)

def trap(self, height):
    ls = len(height)
    if ls < 3: return 0

    volume = 0
    l, r = 0, ls - 1
    l_max, r_max = height[l], height[r]

    while l < r:
        l_max, r_max =  max(height[l], l_max), max( height[r], r_max)
        if l_max <= r_max:
            volume += l_max - height[l]
            l += 1
        else:
            volume += r_max - height[r]
            r -= 1
    return volume