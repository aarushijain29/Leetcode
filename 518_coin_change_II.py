class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[amt][c] = number of ways to make amount = amt using coins[c:]
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]

        # Base case: There is 1 way to make amount 0 using any subset of coins (use no coins)
        # So dp[0][c] = 1 for all c
        dp[0] = [1] * (len(coins) + 1)

        for amt in range(1, len(dp)):
            for c in range(len(coins) - 1, -1, -1):
                # First, copy the number of ways without using coins[c]:
                # This corresponds to skipping coins[c], so we use coins[c+1:]
                dp[amt][c] = dp[amt][c + 1]

                # If amt is large enough to include coins[c], we can also use it
                # Add ways to form (amt - coins[c]) using coins[c:]
                if amt - coins[c] >= 0:
                    dp[amt][c] += dp[amt - coins[c]][c]

                # Now dp[amt][c] = ways to make amt using coins[c:]

        # Final answer: number of ways to make amount using coins[0:]
        return dp[amount][0]
