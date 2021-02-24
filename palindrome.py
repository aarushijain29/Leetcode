class Solution:
    def isPalindrome(self, x: int) -> bool:
        length = length_calc(x)
        reverse_num = reverse(x, length)
        if x<0:
            return False
        else:
            if reverse_num==x:
                return True
            else:
                return False
        
def length_calc(num):
    length = 0
    if num==0:
        length+=1
    while num>0:
        num=num//10 
        length+=1 
    return length

def reverse(num, len):
    reverse_num = 0
    for i in range(len, 0,-1):
        remainder = num%10
        reverse_num+=remainder*(10**(i-1))
        num=num//10
    return reverse_num
