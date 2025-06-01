class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        cur_grp = []

        # finds palindromic substrings starting at s[i]
        def backtrack(i):
            # we have explored all of string s so current group stores all palindromic substrs
            # which we can append to res and finish exploring
            if i >= len(s):
                res.append(cur_grp.copy())
                return
            
            # current group holds all palindromic substrs till s[i] (not incl)
            # we will find all palindromic substr starting at idx i
            # we will explore each substr s[i : j] where j = i till len(s)
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    cur_grp.append(s[i:j+1])
                    backtrack(j + 1)
                    cur_grp.pop()


        backtrack(0)
        return res
