class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        cur_combo = []
        res = []

        def backtrack(i, cur_combo, cur_sum):
            if cur_sum == target:
                res.append(cur_combo.copy())
                return
            
            if i == len(candidates) or candidates[i] > target: return
            
            # include candidates[i] in cur_combo
            cur_sum += candidates[i]
            if cur_sum > target: return

            cur_combo.append(candidates[i])
            
            if cur_sum == target: # If the current combination now hits the target, store it
                res.append(cur_combo.copy())
            elif cur_sum < target: # Otherwise, continue with same i since we can reuse the same number
                backtrack(i, cur_combo, cur_sum)
            cur_combo.pop()
            
            # don't include candidates[i] in cur_combo
            backtrack(i + 1, cur_combo, cur_sum - candidates[i])
        
        backtrack(0, cur_combo, 0)
        return res
