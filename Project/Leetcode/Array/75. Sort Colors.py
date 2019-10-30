class Solution:

    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

    # 92%
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # I shift left, trouble, should shift pointer
        pointer = -1
        left, right = 0, len(nums) - 1
        while left < right:
            while nums[right] == 2 and left < right:
                right -= 1
            if nums[left] == 0 and left < right:
                if pointer < 0:
                    left += 1
                else:
                    nums[left], nums[pointer] = nums[pointer], nums[left]
                    pointer += 1
                    left += 1
            elif nums[left] == 1:
                if pointer < 0:
                    pointer = left
                    left += 1
                else:
                    left += 1
            elif nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            # print(nums, pointer, left)
        if nums[left] == 0 and pointer >= 0:
            nums[left], nums[pointer] = nums[pointer], nums[left]
