class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        maxFreq = 0

        for r in range(len(s)):
            windowLen = r - l + 1
            count[s[r]] += 1
            maxFreq = max(maxFreq, count[s[r]])
            
            while windowLen - maxFreq > k:
                count[s[l]] -= 1
                l += 1
                windowLen = r - l + 1
            res = max(res, r - l + 1)

        return res
