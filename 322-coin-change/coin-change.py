class Solution:
    def coins(self,n,l,tar, dp):
        if tar < 0:
            return -1
        if tar == 0:
            return 0
        if dp[tar]!=-1:
            return dp[tar]
        mi = float('inf')
        for j in range(n):
            if(l[j] <= tar):
                mi = min(mi,1+self.coins(n,l,tar-l[j], dp))
        dp[tar] = mi
        return dp[tar]    
    def coinChange(self, l: List[int], tar: int) -> int:
        n = len(l)
        dp = [-1]*(tar+1)
        if(self.coins(n,l,tar, dp) >= float('inf')):
            return -1
        else:
            return self.coins(n,l,tar, dp) 
        