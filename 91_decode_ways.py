class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {}

        def dfs(i): # number of ways to decode str starting at idx i
            if i >= len(s): # reached end of str i.e. str is valid
                return 1
            if s[i] == '0': # found lone 0 i.e. str is invalid
                return 0
            
            if i in cache:
                return cache[i]
            
            res = dfs(i + 1) # consider digit s[i + 1]
            if i + 1 < len(s):
                if s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456'):
                    res += dfs(i + 2) # consider number s[i + 1 : i + 2 + 1]
            
            cache[i] = res
            return cache[i]
        

        return dfs(0)
