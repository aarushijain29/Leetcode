class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def cleanUp(s):
            i = len(s) - 1
            res = ""
            numHash = 0

            while i >= 0:
                if s[i] != '#':
                    res += s[i]
                    i -= 1
                while i >= 0 and s[i] == '#':
                    numHash += 1
                    i -= 1
                if numHash > 0:
                    while i >= 0 and numHash > 0:
                        if s[i] != '#':
                            numHash -= 1
                        else:
                            numHash += 1
                        i -= 1
            
            return res

        return cleanUp(s) == cleanUp(t)
                
                
