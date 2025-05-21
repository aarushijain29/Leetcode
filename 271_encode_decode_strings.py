class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += (str(len(s)) + '#' + s)
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        num = ""
        i = 0
        while i < len(s) - 1:
            if '0' <= s[i] <= '9':
                num += s[i]
                i += 1
            if s[i] == '#':
                res.append(s[i + 1:i + 1 + int(num)])
                i = i + 1 + int(num)
                num = ""
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
