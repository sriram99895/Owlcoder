class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n-1
        print(n)
        while i<j:
            if s[i] == s[j]:
                while s[i] == s[j]:
                    i+=1
                    if i == j:
                        return 0
                while s[j] == s[i-1]:
                    j-=1
            else:
                return j-i+1
        if i == j:
            return 1  
                         
        