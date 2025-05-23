class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        max_len = 0
        l = 0
        highest_freq = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            # highest frequency in s[l : r + 1]
            highest_freq = max(highest_freq, freq_map[s[r]])

            # shrink window when more than k replacements needed to make substr valid
            # num replacements = cur substr len - highest freq in cur substr
            while r - l + 1 - highest_freq > k:
                freq_map[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        
        return max_len
