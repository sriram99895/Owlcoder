class Solution:
    import math
    def solve(self,n,dp):
        if n == 0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        mi = 9999999    
        for i in range(1,int(math.sqrt(n)+1)):
            if i*i<=n:
                mi = min(mi,1+self.solve(n-i*i,dp))
        dp[n]= mi        
        return dp[n]
    def numSquares(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        d = self.solve(n,dp)
        return d
        