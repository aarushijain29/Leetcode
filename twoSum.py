class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashTable:
                return [i, hashTable[diff]]
            hashTable[nums[i]] = i
