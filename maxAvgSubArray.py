class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = [0]

        for i in range(k): # k <= n
            window[0] += nums[i]
        window[0] /= k
    
        if k < len(nums):
            for i in range(1, len(nums) - k + 1):
                s = window[-1] + (nums[i + k - 1] - nums[i - 1])/k
                window.append(s)
        
        return max(window)
        
