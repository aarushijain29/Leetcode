class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            # num = starting element of a potential consecutive subsequence
            if num - 1 not in num_set: 
                cur_len = 1
                while num + 1 in num_set:
                    cur_len += 1
                    num += 1
                max_len = max(max_len, cur_len)
        
        return max_len
