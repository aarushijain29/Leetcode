class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        len = 0
        single = False
        for char, num in d.items():
            remainder = num%2
            len += (num - remainder)
            if remainder == 1:
                len += 1
                single = True
        
        return len
