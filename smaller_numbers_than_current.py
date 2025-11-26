class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        map_nums = {}

        for i in range(len(nums)):
            num = sort_nums[i]
            if num not in map_nums:
                map_nums[num] = i
        
        result = [0] * len(nums)
        
        for i in range(len(nums)):
            result[i] = map_nums[nums[i]]
        
        return result
