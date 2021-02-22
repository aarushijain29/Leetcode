class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(0,len(nums)):
            first = nums[j]
            for i in range(j+1, len(nums)):
                if target==first+nums[i]:
                    return [j,i]
