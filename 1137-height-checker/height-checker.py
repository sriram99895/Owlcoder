class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        k = sorted(heights)
        c = 0
        for i in range(len(k)):
            if k[i]!= heights[i]:
               c+=1
        return c    
        