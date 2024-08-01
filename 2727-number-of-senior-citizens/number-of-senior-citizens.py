class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c = 0
        for i in details:
            s=int(i[11]+i[12])
            if s>60:
                c+=1
        return c        
        