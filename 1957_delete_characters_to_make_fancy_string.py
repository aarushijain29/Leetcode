class Solution:
    def makeFancyString(self, s: str) -> str:
        left = 0
        res = []

        cur_count = 0
        for right in range(len(s)):
            if s[left] == s[right]:
                cur_count += 1
            else:
                left = right
                cur_count = 1

            if cur_count < 3:
                res.append(s[right])
        
        return ''.join(res)
