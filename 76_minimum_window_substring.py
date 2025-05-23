class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        t_len, s_len = len(t), len(s)

        if t_len > s_len:
            return res

        res_idx = None
        matches = 0
        t_freq = Counter(t)
        s_freq = defaultdict(int)
        l = 0

        for r in range(s_len):
            # if s[r] is not in t, we can ignore it
            # so our logic needs to be applied only when we see s[r] in t
            if s[r] in t_freq:

                s_freq[s[r]] += 1
                # if freq of s[r] in cur substr = freq of s[r] in t
                # then we have a match for one char hence matches += 1
                if s_freq[s[r]] == t_freq[s[r]]:
                    matches += 1
                
                # we have exact number of matches needed
                # now we can explore shrinking our window to find min window
                while matches == len(t_freq):
                    # if min window is larger than cur window, update min
                    if not res_idx or r - l + 1 < res_idx[1] - res_idx[0] + 1:
                        res_idx = [l, r]
                    # decrement s[l] freq to shrink window    
                    s_freq[s[l]] -= 1
                    # if s[l] is in t then we may lose a match since
                    # s[l] freq is lesser now so we need to update matches
                    if s[l] in t_freq and s_freq[s[l]] < t_freq[s[l]]:
                        matches -= 1
                    l += 1

        if res_idx:
            res = s[res_idx[0]:res_idx[1] + 1]
        return res 
