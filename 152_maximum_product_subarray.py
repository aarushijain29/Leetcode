class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_prod: stores the overall maximum prod found so far
        # max_so_far: max prod of a subarray ending at the curr pos
        # min_so_far: min prod of a subarray ending at the curr pos (for negatives)
        max_prod = max_so_far = min_so_far = nums[0]

        for right in range(1, len(nums)):
            cur = nums[right]

            # Multiply curr number with both max and min so far (from previous step)
            # This is because a negative * negative can become the new max

            # max_so_far = prod of nums from left to right - 1 (incl.)
            # cur_max_so_far = prod of nums from left to right (incl.)
            cur_max_so_far = max_so_far * cur
            cur_min_so_far = min_so_far * cur
            
            max_so_far = max(cur, cur_max_so_far, cur_min_so_far)
            min_so_far = min(cur, cur_max_so_far, cur_min_so_far)

            max_prod = max(max_prod, max_so_far)
        
        return max_prod
