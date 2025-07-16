class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        # dp[i][j] = len of LCS between text1[i:] and text2[j:]
        # Extra row and column for easier bounds handling (padding with 0s at the end)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        # Fill the dp table in reverse (bottom-up)
        for t1 in range(len1 - 1, -1, -1):
            for t2 in range(len2 - 1, -1, -1):
                # We are comparing text1[t1:] with text2[t2:]
                if text1[t1] == text2[t2]:
                    # If characters match, we can include them in the LCS
                    # So LCS(text1[t1:], text2[t2:]) = 1 + LCS(text1[t1+1:], text2[t2+1:])
                    dp[t1][t2] = 1 + dp[t1 + 1][t2 + 1]
                else:
                    # If characters don't match, take the best of:
                    # - Skipping text1[t1] = LCS(text1[t1+1:], text2[t2:])
                    # - Skipping text2[t2] = LCS(text1[t1:], text2[t2+1:])
                    dp[t1][t2] = max(dp[t1 + 1][t2], dp[t1][t2 + 1])

        return dp[0][0]
