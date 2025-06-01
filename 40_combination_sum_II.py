class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur_combo = []
        res = []

        def backtrack(i, cur_combo, cur_sum):
            if cur_sum == target:
                res.append(cur_combo.copy())
                return 
            
            if i == len(candidates) or candidates[i] > target:
                return
            
            # include candidates[i] in current combo
            cur_sum += candidates[i]
            if cur_sum > target:
                return
            
            cur_combo.append(candidates[i])
            if cur_sum == target:
                res.append(cur_combo.copy())
            else:
                backtrack(i + 1, cur_combo, cur_sum)

            # don't include candidates[i] (and duplicates) in current combo
            cur_combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur_combo, cur_sum - candidates[i])

        backtrack(0, cur_combo, 0)
        return res
