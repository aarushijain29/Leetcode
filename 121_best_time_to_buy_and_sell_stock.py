class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            # maximise profit using buy and sell = prices[i]
            max_profit = max(max_profit, prices[i] - buy)
            # if lower price found, make it new buy price
            buy = min(buy, prices[i])

        return max_profit
