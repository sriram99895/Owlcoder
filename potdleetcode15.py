class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wd = {}
        ld = {}
        emp = []
        nl = []
        sl = []
        for i in matches:
            if i[0] not in wd:
                wd[i[0]] = 1
            else:
                wd[i[0]]+=1
            if i[1] not in ld:
                ld[i[1]] = 1
            else:
                ld[i[1]]+=1
        for k,v in wd.items():
            if k not in ld:
                nl.append(k)
        for k,v in ld.items():
            if v == 1:
                sl.append(k)  
        nl.sort()
        sl.sort()                      
        emp.append(nl)
        emp.append(sl)               
        # print(wd)
        # print(ld)  
        return  emp     
