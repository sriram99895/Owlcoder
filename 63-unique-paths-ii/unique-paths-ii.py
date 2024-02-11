class Solution:
    def sub(self,i,j,n,m,l,dp):
        if i==n-1 and j == m-1:
            if l[i][j]!=1:
                return 1
            else:
                return 0    
        if i>n-1 or j>m-1:
            return 0    
        if l[i][j] == 1:
            return 0
        if dp[i][j] !=-1:
            return dp[i][j]
        dp[i][j] = self.sub(i+1,j,n,m,l,dp)+self.sub(i,j+1,n,m,l,dp)
        return dp[i][j]            
    def uniquePathsWithObstacles(self, l: List[List[int]]) -> int:
        global dp
        dp = [[-1]*101 for i in range(101)]
        n = len(l)
        m = len(l[0])
        k = self.sub(0,0,n,m,l,dp)
        return k

        