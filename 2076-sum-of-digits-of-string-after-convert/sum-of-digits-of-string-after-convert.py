class Solution:
    def getLucky(self, s: str, t: int) -> int:
        p = 0
        for i in s:
            k=ord(i)-96
            while k:
                p+=k%10
                k = k//10
        t = t -1
        print(t)
        n = 0
        while t:
            t = t-1
            while p:
                n+=p%10
                p = p//10
            p = n  
            n = 0
        return p    



        