class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""

        for char in s:
            if char.isalnum():
                a += char
        a = a.lower()
        a = a.replace(" ", "")
        return a[::-1] == a
