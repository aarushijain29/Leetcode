class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = length of the LIS starting at index i
        dp = [1] * len(nums)  # the shortest LIS including just nums[i] is of length 1

        # Iterate backwards so we can build dp[start] based on dp[end] where end > start
        for start in range(len(nums) - 2, -1, -1):
            # For current nums[start], we try extending it by checking elements to its right
            # i.e. checking all nums[end] where end > start
            for end in range(start + 1, len(nums)):
                # We're considering subsequences of the form [nums[start], ..., nums[end]]
                # which is nums[start:end+1]
                if nums[start] < nums[end]:
                    # nums[start] < nums[end] means we can append nums[end] after nums[start]
                    # So possible subsequence = [nums[start]] + LIS starting from nums[end]
                    # i.e. trying to build on top of nums[start:end+1]
                    dp[start] = max(dp[start], 1 + dp[end])  # update dp[start] if longer LIS is found

        return max(dp)
