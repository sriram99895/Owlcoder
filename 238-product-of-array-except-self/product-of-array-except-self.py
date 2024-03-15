class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        for i in nums:
            if  i!=0:
                p*=i     
        l = []
        z = nums.count(0)
        if z == 0:
            for i in nums:
                l.append(p//i)
        elif z == 1:
            for i in nums:
                if i == 0:
                    l.append(p)
                else:
                    l.append(0)
        else:
            n = len(nums)
            for i in range(n):
                l.append(0)
        return l        

            

         
        