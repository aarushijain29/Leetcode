class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # array not rotated
        if nums[0] < nums[-1]:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2
            if nums[left] <= nums[right]:
                return nums[left]
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid       
