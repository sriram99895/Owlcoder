class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        i = 0
        j = len(s) -1
        while i<=j:
            if a[i] < a[j]:
                a[j] = a[i]
            else:
                a[i] = a[j]
            i+=1
            j-=1
        return "".join(a)            
        
        