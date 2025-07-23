class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        max_gain = 0

        d = [('ab', x), ('ba', y)]
        if y > x:
            d[0], d[1] = d[1], d[0]

        for (s1, s2), pts in d:
            stack = []
            for c in s:
                if len(stack) >= 1 and stack[-1] == s1 and c == s2:
                    stack.pop()
                    max_gain += pts
                else:
                    stack.append(c)
            s = ''.join(stack)

        return max_gain
