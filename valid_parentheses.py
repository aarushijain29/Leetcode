class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        d = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for i in s:
            if i in d:
                l.append(i)
            elif len(l) == 0 or d[l.pop(-1)] != i:
                return False

        return len(l) == 0
