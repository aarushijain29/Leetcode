class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m - 1)]
        dp.append([1] * n)

        for r in range(m - 2, -1, -1):
            dp[r][-1] = 1
            for c in range(n - 2, -1, -1):
                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]
        
        return dp[0][0]
