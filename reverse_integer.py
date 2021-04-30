class Solution:
    def reverse(self, x: int) -> int:
        revnum = reversal(x)
        if (-(2 ** 31) > revnum) or (revnum > (2 ** 31) - 1):
            return 0
        else:
            return revnum        
        
def reversal(x):
    revnum = 0
    if x<0:
        return (-1)*Solution().reverse(-x)
    else:
        remainder = 0
        i = 0  
        while x!=0:
            remainder = x%10
            x=x//10
            revnum = revnum*10 + remainder
    return revnum
