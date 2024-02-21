class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x= str(x)
        # return x == x[::-1]
        s = 0
        t = x
        while t>0:
            r = t%10
            s= s*10+r 
            t = t//10
        return x==s    