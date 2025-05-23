class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = 0
        # stores the last occurrence (index) of a char
        char_recent_idx = {}

        for r in range(len(s)):

            # s[r] already found in substr
            # need to shrink window till no duplicates in s[l : r + 1]

            if s[r] in char_recent_idx:
                # Update l only if duplicate char is in the current window
                # max prevents moving l backwards to not include duplicates
                l = max(l, char_recent_idx[s[r]] + 1)

            char_recent_idx[s[r]] = r
            # cur substr: s[l : r + 1]
            max_len = max(max_len, r - l + 1)

        return max_len
