#no of laser beams in a bank in leetcode
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l = []
        for i in range(len(bank)):
            c = 0
            for j in range(len(bank[i])):
                if bank[i][j] == '1':
                    c+=1
            if c>0:
                l.append(c)
        ans = 0
        for i in range(1,len(l)):
            ans+=l[i-1]*l[i] 
        return ans         

