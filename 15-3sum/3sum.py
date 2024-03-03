class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        nums.sort()
        i=0
        j=i+1
        k=len(nums)-1
        s=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
            
                if nums[i]+nums[j]+nums[k]==0:
                    l=nums[i],nums[j],nums[k]
                    s.append(l)
                    k-=1
                elif nums[i]+nums[j]+nums[k]>=0:
                    k-=1
                else:
                    j+=1  
        o=set(s)
        return list(o)                       
                        
        