class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closeN, path):
            if openN == closeN == n:
                res.append(path)
            if openN < n:
                backtrack(openN + 1, closeN, path + '(')
            
            if closeN < openN:
                backtrack(openN, closeN + 1, path + ')')

        backtrack(0, 0, "")
        return res                
