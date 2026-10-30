
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * (n + 1)
        ans = 0

        for row in matrix:
            for i in range(n):
                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = []

            for i in range(n + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    ans = max(ans, h * width)

                stack.append(i)

        return ans
