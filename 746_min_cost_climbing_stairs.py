class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # second_last_step: cost to reach the second last step
        # last_step: cost to reach the last step
        second_last_step = last_step = 0
        for i in range(2, len(cost) + 1):
            # last_step + cost[i - 1]: cost to reach last step and then taking the last step to reach current step
            current_step = min(last_step + cost[i - 1], second_last_step + cost[i - 2])
            second_last_step = last_step
            last_step = current_step
            
        return last_step
