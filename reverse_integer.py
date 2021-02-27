class Solution:
    def reverse(self, x: int) -> int:
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
            
        if -2**(31) <= revnum <= 2**(31) - 1:
            return revnum
            
        else:
            return 0
            

        
