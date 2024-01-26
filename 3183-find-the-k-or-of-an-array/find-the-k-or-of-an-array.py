class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(32):
            c = 0
            for j in range(len(nums)):
                if nums[j] &(1<<i)>0:
                    c+=1
            if c>=k:
                s+=2**i
        return s        

        