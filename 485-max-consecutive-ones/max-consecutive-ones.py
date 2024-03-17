class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        ma = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
            else:
                ma = max(ma,c)
                c = 0
        ma = max(ma,c)            
        return ma