class Solution:
    def myAtoi(self, s: str) -> int:
        num = ''
        sign = ''
        s = s.lstrip()
        if len(s) == 0:
            return 0
        
        if '0' <= s[0] and '9' >= s[0]:
            num = num_form(0, s, num)
        else:
            sign += s[0]
            num = num_form(1, s, num) 
        
        if num == '':
            return 0
        else:
            result = int(num)
            if sign == '-':
                result = (-1)*result
            if (result < (-2)**31):
                result = (-2)**31
            elif (result > ((2)**31) - 1):
                result = ((2)**31) - 1

            return result


def num_form(j, s, num):
    for i in range(j,len(s)):
        if '0' <= s[i] and '9' >= s[i]:
            num += s[i]    
        else:
            break
    return num

