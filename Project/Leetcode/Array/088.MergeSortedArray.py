class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ls = m + n - 1
        i1 = m - 1
        i2 = n - 1
        while ls >= 0 and i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[ls] = nums1[i1]
                i1 -= 1
                ls -= 1
            else:
                nums1[ls] = nums2[i2]
                i2 -= 1
                ls -= 1
        while i2 >= 0:
            nums1[ls] = nums2[i2]
            i2 -= 1
            ls -= 1
        return nums1



if __name__ == '__main__':
    S = Solution()
    # a = S.merge([1,2,3,0,0,0], 3, [2,2,3], 3)
    # a = S.merge([1,2,3,0,0,0],3, [2,5,6], 3)
    a = S.merge([0], 0, [1], 1)
    print(a)