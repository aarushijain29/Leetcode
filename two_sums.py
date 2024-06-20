class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictNums = {}

        for i in range(len(nums)):
            if nums[i] in dictNums:
                dictNums[nums[i]].append(i)
            else:
                dictNums[nums[i]] = [i]

        for key, item in dictNums.items():
            complement = target - key
            if complement in dictNums:
                if len(dictNums[complement]) > 1:
                    return dictNums[complement]
                elif complement != key:
                    l = item + dictNums[complement]
                    return l
