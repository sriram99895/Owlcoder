class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        p = (len(edges))
        d ={}
        for i in edges:
            for j in i:
                if j not in d:
                    d[j] = 1
                else:
                    d[j]+=1
        for k,v in d.items():
            if v == p:
                return k                
        return 1        
        