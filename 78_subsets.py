class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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

            # dont include nums[i] in current subset
            cur_set.pop() # must remove last element as cur_set[-1] = nums[i]
            backtrack(i + 1, cur_set)
        
        backtrack(0, cur_set)
        return res
