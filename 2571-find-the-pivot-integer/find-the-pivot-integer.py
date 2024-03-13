class Solution:
    def pivotInteger(self, n: int) -> int:
        s = n*(n+1)//2
        p = 0
        for i in range(n+1):
            p+=i
            if s == p:
                return i
            s-= i
        return -1        
