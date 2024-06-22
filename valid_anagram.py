class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for char in t:
            if char in d:
                d[char] -= 1
            else:
                return False
        
        for key,item in d.items():
            if item != 0:
                return False
            
        return True
