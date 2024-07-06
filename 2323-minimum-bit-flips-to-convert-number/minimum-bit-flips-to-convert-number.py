class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        k = start^goal
        c = 0
        while k:
            c+=1
            k = k&(k-1)
        return c    
        