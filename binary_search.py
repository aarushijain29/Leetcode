class Solution:

    def search_help(self, nums: List[int], target: int, start: int, end: int) -> int:

        if start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return self.search_help(nums, target, 0, mid - 1)
            else:
                return self.search_help(nums, target, mid + 1, end)

        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.search_help(nums, target, 0, len(nums) - 1)
