class Solution:
    def fibi(self,n):
        if n <= 1:
            return n    
        a = self.fibi(n-1)
        b = self.fibi(n-2)
        return a+b    
    def fib(self, n: int) -> int:
        k = self.fibi(n)
        return k
        