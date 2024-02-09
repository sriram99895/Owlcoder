class Solution:
    def tri(self,n,dp):
        if n <=1:
            return n
        if n==2:
            return 1
        if dp[n]!=-1:
            return dp[n]
        c = self.tri(n-1,dp)
        a = self.tri(n-2,dp)
        b = self.tri(n-3,dp)   
        dp[n] = a+c+b
        return dp[n]    
    def tribonacci(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        k = self.tri(n,dp)
        return k
        