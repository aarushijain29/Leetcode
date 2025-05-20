class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums_map:
                return [i, nums_map[complement]]
            nums_map[nums[i]] = i
        
        return []
