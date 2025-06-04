class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_idx = [0, 0]

        for i in range(len(s)):
            # odd len palindrome centred at i
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if res_idx[1] - res_idx[0] + 1 < r - l + 1:
                    res_idx = [l, r]
                l -= 1
                r += 1
            
            # even len palindrome centred at i and i + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if res_idx[1] - res_idx[0] + 1 < r - l + 1:
                    res_idx = [l, r]
                l -= 1
                r += 1
        
        return s[res_idx[0] : res_idx[1] + 1]          
