class Solution:
    def div(self,n):
        t = n
        while t:
            k = t%10
            if k == 0:
                return 0
            if n%k != 0:
                return 0
            t = t//10
        return 1        
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left,right+1):
            if self.div(i) == 1:
                l.append(i)
        return l        
        
        