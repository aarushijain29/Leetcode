class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        letter_map = {
            2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'
        }
        
        res = []
        cur_combo = []

        # O(N * 4^N)
        def backtrack(i):
            if i >= len(digits):
                res.append(''.join(cur_combo)) # O(N); N = len(digits)
                return 
            digit = int(digits[i])
            # O(4^N); 4 is the max len of letters in letter_map
            # for each digit, we have to explore at most 4 letters
            # we have to do this N times as each digit corresponds to one letter
            for letter in letter_map[digit]:
                cur_combo.append(letter)
                backtrack(i + 1)
                cur_combo.pop()
        
        backtrack(0)
        return res
