class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n&1
        n = n>>1
        while(n):
            next = n&1
            if prev>0 and next > 0:
                return 0
            elif prev == 0 and next == 0:
                return 0
            prev = next    
            n = n>>1 
        return 1       
        
n  = int(input())
k = Solution()
print(Solution.hasAlternatingBits(n));
        