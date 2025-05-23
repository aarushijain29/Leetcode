class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2: return False
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(l1):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
            
        l = 0
        for r in range(l1, l2):
            if freq1 == freq2:
                return True
            freq2[ord(s2[r]) - ord('a')] += 1
            freq2[ord(s2[l]) - ord('a')] -= 1
            l += 1
        
        return freq1 == freq2
