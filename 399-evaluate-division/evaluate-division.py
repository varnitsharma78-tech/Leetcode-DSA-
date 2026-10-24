
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = {}

        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}

            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)

                    if result != -1.0:
                        return value * result

            return -1.0

        ans = []

        for a, b in queries:
            ans.append(dfs(a, b, set()))

        return ans
