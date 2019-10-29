class Solution:
    # 98%
    def summaryRanges(self, nums) :
        if not nums: return []
        ranges = []
        temp_r = [str(nums[0])]
        i = 1
        while i < len(nums):
            if str(nums[i] - 1) not in temp_r:
                ranges.append(temp_r)
                temp_r = []
            # Make sure there is always 2 number in the list, substitute last number into new one
            if len(temp_r) == 2:
                temp_r.pop()
            temp_r.append(str(nums[i]))
            i += 1

        ranges.append(temp_r)
        print(ranges)
        print('->'.join(map(str, ['0', '2'])))
        return ['->'.join(map(str, r)) for r in ranges]
if __name__ == '__main__':
    S = Solution()
    test = S.summaryRanges([0,1,2,4,5,7])
    print(test)