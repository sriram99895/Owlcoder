class Solution:
    def fibi(self,n,dp):
        if n <= 1:
            return n  
        if dp[n]!=-1:
            return dp[n]      
        a = self.fibi(n-1,dp)
        b = self.fibi(n-2,dp)
        dp[n] = a+b
        return dp[n]    
    def fib(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        k = self.fibi(n,dp)
        return k
        