class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        v = "aeiou"
        for i in range(k):
            if s[i] in v:
                c+=1
        ma = c
        for i in range(k,len(s)):
            if s[i-k] in v:
                c-=1
            if s[i] in v:
                c+=1
            ma = max(c,ma)
        return ma            


        
        