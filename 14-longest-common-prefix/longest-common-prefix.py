class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sp = strs[0]
        m = 999999
        for i in strs:
            m = min(m,len(i))
        print(m)    
        k = sp[:m]
        ma =99999
        for i in strs:
            c = 0
            for j in range(m):
                if i[j] == k[j]:
                    c+=1
                else:
                    break 
            if c == 0:
                return ""
            ma = min(ma,c)               
        return sp[:ma]            
        