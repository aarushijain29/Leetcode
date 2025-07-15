class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = amount + 1
        dp = {0:0}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            res = MAX
            for coin in coins:
                if amount >= coin:
                    res = min(res, 1 + dfs(amount - coin))

            dp[amount] = res
            return dp[amount]
                    
        dfs(amount)    
        return dp[amount] if dp[amount] != MAX else -1
