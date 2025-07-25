class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
            
        return sum(set([num for num in nums if num > 0]))
