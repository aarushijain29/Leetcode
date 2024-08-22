class Solution:
    # tracking frequence of alphabets in each string to group anagrams i.e. words which have the same frequency of letters
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) in [0,1]:
            return [strs]

        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return res.values()
    # sorting words in strs to group anagrams i.e. words which are the same after sorting
    def groupAnagramsUsingSort(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for s in strs:
            sorted_s = str(sorted(s))
            d[sorted_s].append(s)

        return d.values()
