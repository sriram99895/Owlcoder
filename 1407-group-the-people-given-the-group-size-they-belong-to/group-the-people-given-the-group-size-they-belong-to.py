class Solution:
    def groupThePeople(self, l: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(l)):
            if l[i] not in d:
                d[l[i]] = [i]
            else:
                d[l[i]].append(i) 
        emp = []
        for k,v in d.items():
            p = []
            for i in range(len(v)):
                if len(p) == k:
                    emp.append(p)
                    p = [v[i]]
                else:
                    p.append(v[i])
            emp.append(p)

        return emp    
        