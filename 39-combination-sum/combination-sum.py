class Solution:
    def combi(self,i,n,tar,l,m,ml):
        if i == n:
            if tar == 0:
                c=m.copy()
                ml.append(c)
            return 
        if tar>=l[i]:
            m.append(l[i])
            self.combi(i,n,tar-l[i],l,m,ml)
            m.pop()
        self.combi(i+1,n,tar,l,m,ml)       
    def combinationSum(self, l: List[int], tar: int) -> List[List[int]]:
        n = len(l)
        ml = []
        m = []
        self.combi(0,n,tar,l,m,ml)
        return ml
        