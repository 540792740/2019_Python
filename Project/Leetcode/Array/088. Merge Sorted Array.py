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
        m = m - 1
        n = n - 1
        while ls > 0 and n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[ls] = nums1[m]
                m -= 1
                ls -= 1
            else:
                nums1[ls] = nums2[n]
                n -= 1
                ls -= 1
        while n >= 0:
            nums1[ls] = nums2[n]
            n -= 1
            ls -= 1
        return nums1

if __name__ == '__main__':
    S = Solution()
    a = S.merge([1,2,3,0,0,0],3, [2,5,6], 3)
    a = S.merge([0],0,[1],1)
    print(a)