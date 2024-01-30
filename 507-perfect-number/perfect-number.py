class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n==1:
            return 0
        k = int(math.sqrt(n))
        s = 1
        for i in range(2,k+1):
            if n%i == 0:
                if n//i != i:
                    s+=i
                    s+=n//i
                else:
                    s+=i
        return s == n                       
                