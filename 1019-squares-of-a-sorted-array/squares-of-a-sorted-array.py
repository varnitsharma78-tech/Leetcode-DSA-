class Solution:

    def sortedSquares(self, nums: list[int]) -> list[int]:

        result = []

        for num in nums:
            result.append(num * num)

        result.sort()

        return result