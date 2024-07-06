class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # make a set of nums to get unique nums
        numSet = set(nums)
        
        maxLen = 1
        for num in numSet:
            seqLen = 0
            if num - 1 not in numSet: # num is the start of a sequence
                while num in numSet:
                    seqLen += 1
                    num += 1
                maxLen = max(maxLen, seqLen)      

        return maxLen
