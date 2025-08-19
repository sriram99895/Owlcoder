class Solution:
    def func(self,z):
        k = z*(z+1)//2
        return k
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        c = 0
        z = 0
        for i in nums:
            if i == 0:
                z+=1
            else:
                c+=self.func(z)
                z = 0
        if z>0:
            c+=self.func(z)
        return c      
        