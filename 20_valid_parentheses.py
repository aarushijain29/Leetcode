class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '[':']', '{':'}'}

        for c in s:
            if c in brackets:
                stack.append(c)
            elif not stack or brackets[stack.pop(-1)] != c:
                return False
        
        return len(stack) == 0
