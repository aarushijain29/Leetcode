class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur_set = []

        def backtrack(i, cur_set):
            nonlocal res
            if i == len(nums):
                res.append(cur_set.copy())
                return
            
            # include nums[i] in current subset
            cur_set.append(nums[i])
            backtrack(i + 1, cur_set)

            # don't include nums[i] in current subset
            cur_set.pop()
            # don't include duplicates of nums[i] either
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, cur_set)
        
        backtrack(0, cur_set)
        return res
