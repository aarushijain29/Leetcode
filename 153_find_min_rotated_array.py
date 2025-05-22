class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l)//2
            # nums[l:r] is sorted
            if nums[l] <= nums[r]:
                return nums[l]

            # since nums smaller than nums[m] exist right of m, 
            # min(nums) will be found in nums[m + 1:r]
            if nums[m] > nums[r]:
                l = m + 1
                
            # since nums[m] is smaller than all nums right of it
            # min(nums) will be found in nums[l:m]
            # (nums[m] can also be min(nums))
            elif nums[m] <= nums[r]:
                r = m
