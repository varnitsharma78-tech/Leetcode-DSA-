class Solution:

    def moveZeroes(self, nums: list[int]) -> None:

        index = 0

        for x in nums:
            if x != 0:
                nums[index] = x
                index += 1

        while index < len(nums):
            nums[index] = 0
            index += 1
            