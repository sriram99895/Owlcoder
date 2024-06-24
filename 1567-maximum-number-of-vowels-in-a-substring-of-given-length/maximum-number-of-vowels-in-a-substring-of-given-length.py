class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        c  = 0
        a = "aeiou"
        for i in range(k):
            if s[i] in a :
                c+=1
        ma = c        
        i = 0
        j = k       
        while j<n:
            if s[j] in a and s[i] not in a:
                c+=1

            elif s[j] not in  a and s[i] in a:
                c-=1
            i+=1
            j+=1     
            ma = max(ma,c)      
        return ma


