class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        k= int(math.log2(num))+1
        kn = 2**k-1
        return (kn^num)
        
