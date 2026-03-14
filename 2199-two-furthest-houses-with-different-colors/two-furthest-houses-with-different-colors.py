class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i = 0
        j = len(colors)-1
        m = 0
        while(i<j):
            if colors[i]==colors[j]:
                i+=1
            else:
                m = max(m,j-i)
                j-=1
                # continue
            # j-=1 
        k = 0
        i =0
        j = len(colors)-1
        while(i<j):
            if colors[i]==colors[j]:
                j-=1
            else:
                k = max(k,j-i)
                i+=1
                # continue  
        return max(k,m)           