class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
       prev = math.sqrt(d[0][0]**2 + d[0][1]**2)
       pro =  d[0][0]*d[0][1]
       for i in range(1,len(d)):
           m = math.sqrt(d[i][0]**2 + d[i][1]**2)
           if m>prev:
              print(m,prev)
              prev = m
              pro = d[i][0]*d[i][1]
           elif m == prev:
              pro = max(pro,d[i][0]*d[i][1])   
       return pro       
           



        

        