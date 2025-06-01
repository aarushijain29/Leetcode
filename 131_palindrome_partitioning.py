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
        dp = [[0 for i in range(len(s))] for i in range(len(s))]

        # finds palindromic substrings starting at s[i]
        def backtrack(i):
            # we have explored all of string s so current group stores all palindromic substrs
            # which we can append to res and finish exploring
            if i >= len(s):
                res.append(cur_grp.copy())
                return
            
            # current group holds all palindromic substrs till s[i] (not incl)
            # we will find all palindromic substr starting at idx i
            # we will explore each substr starting at index i
            # O(2^N); N = len(s)
            # at each idx i we have two choices - to partition or not partition at i i.e. total 2^N choices
            for j in range(i, len(s)):
                if dp[i][j] == 1 or is_palindrome(i, j):
                    dp[i][j] == 1
                    cur_grp.append(s[i:j+1]) # O(N); N = len(s)
                    backtrack(j + 1)
                    cur_grp.pop()
            
            # total time complexity: O(N * 2^N)
            # space: O(N) as recursion stack can go as deep as N
            # when all substrings are one char each


        backtrack(0)
        return res
