class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        first = 0
        for i in range(length):
            first += nums[i]
            result.append(first)
        return result
