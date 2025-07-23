class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        max_sum = cur_sum = nums[left]
        seen = set([nums[left]])
        
        for right in range(1, len(nums)):
            while left <= right and nums[right] in seen:
                cur_sum -= nums[left]
                seen.remove(nums[left])
                left += 1

            cur_sum += nums[right]
            seen.add(nums[right])
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
