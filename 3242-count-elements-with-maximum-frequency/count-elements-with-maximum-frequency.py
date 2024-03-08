class Solution:
    def maxFrequencyElements(self, l: List[int]) -> int:
        d = {}
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        c = 0        
        e = max(d.values())
        for k,v in d.items():
            if v == e:
                c+=e
        return c                    
        