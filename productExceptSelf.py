class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # create array right where right[i] == the product of all numbers to the right of nums[i]
        right = [1 for i in range(length)]
        for i in range(length-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        # create array left where left[i] == the product of all numbers to the left of nums[i]
        left = [1 for i in range(length)]
        for i in range(1,length):
            left[i] = left[i-1]*nums[i-1]
        # return array result where result[i] == left[i]*right[i]
        return [left[i]*right[i] for i in range(length)]
