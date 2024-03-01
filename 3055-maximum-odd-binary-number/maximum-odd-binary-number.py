class Solution:
    def maximumOddBinaryNumber(self, k: str) -> str:
        z = 0
        c = 0
        s=""
        for i in k:
            if i == "1":
                c+=1
            else:
                z+=1
        for i in range(c-1):
            s+="1"
        for i in range(z):
            s+="0"
        if c>0:
            s+='1'    
        return s                   
        