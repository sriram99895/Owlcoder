class Solution:
    def fun(self,i,j,m,n,dp):
        if i == m-1 and j == n-1:
            return 1
        if i>m-1 or j> n-1:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        k = self.fun(i+1,j,m,n,dp) + self.fun(i,j+1,m,n,dp) 
        dp[i][j] = k
        return dp[i][j]        
    def uniquePaths(self, m: int, n: int) -> int:
        global dp
        dp = [[-1]*101 for i in range(101)]
        k = self.fun(0,0,m,n,dp)
        return k
