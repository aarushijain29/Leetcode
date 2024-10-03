class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]*n

        for i in range(n):
            while stack and temperatures[i] > stack[-1][0]:
                t = stack.pop()
                res[t[1]] = i - t[1]
            stack.append((temperatures[i], i))

        return res
