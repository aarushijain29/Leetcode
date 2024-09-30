class Solution:
    def digitSquare(self, n: int) -> int:
        res = 0
        while n != 0:
            remainder = n%10
            res += remainder*remainder
            n = n//10
        return res

    def isHappy(self, n: int) -> bool:
        
        slow = self.digitSquare(n)
        fast = self.digitSquare(slow)
        while fast != slow and fast != 1:
            slow = self.digitSquare(slow)
            fast = self.digitSquare(self.digitSquare(fast))

        return fast == 1
