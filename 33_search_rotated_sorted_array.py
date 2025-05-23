class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l)//2

            if nums[m] == target:
                return m
            # nums[l:m] is sorted
            elif nums[l] <= nums[m]:
                # target is in nums[l:m]
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # target is after nums[l:m] i.e. in nums[m + 1:r]
                else:
                    l = m + 1
            # nums[m + 1:r] is sorted 
            else:
                # target is in nums[m + 1:r]
                if nums[m] < target <= nums[r]:
                    l = m + 1
                # target is before nums[m:r] i.e. in nums[l:m - 1]
                else:
                    r = m - 1


        return -1
