class Solution:

    def duplicateZeros(self, arr: list[int]) -> None:

        i = 0

        while i < len(arr):

            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1

            i += 1