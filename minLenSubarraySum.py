class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = len(nums) + 1
        s = 0

        for r in range(len(nums)):
            # s = sum of sliding window from nums[l] to nums[r]
            s += nums[r]
            # while sliding window is valid i.e. sum is greater than or equal to target
            while s >= target:
                # store the minimum of current and previous valid sliding window len
                minLen = min(minLen, r - l + 1)
                # to move sliding window forward while shrinking it to find the smallest window:
                # step 1: subtract the element going out of the window to avoid recalculation of common nums
                s -= nums[l]
                # step 2: move window forward while keeping window end (r) the same to shrink the window
                l += 1
        
        return minLen if minLen != len(nums) + 1 else 0
