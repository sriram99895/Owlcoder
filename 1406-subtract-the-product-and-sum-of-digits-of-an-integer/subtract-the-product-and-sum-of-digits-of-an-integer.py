class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n:
            d = n%10
            s+=d
            p*=d
            n = n//10
        return p-s        
        