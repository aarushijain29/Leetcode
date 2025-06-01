class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_perm = []
        visited = set()

        def backtrack(cur_perm):
            if len(cur_perm) == len(nums):
                res.append(cur_perm.copy())
                return

            for i in range(len(nums)):
                if i not in visited:
                    cur_perm.append(nums[i])
                    visited.add(i)
                    backtrack(cur_perm)
                    visited.remove(i)
                    cur_perm.pop()
        
        backtrack(cur_perm)
        return res
