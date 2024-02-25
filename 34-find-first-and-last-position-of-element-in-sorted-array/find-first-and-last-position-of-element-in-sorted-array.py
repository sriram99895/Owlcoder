class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        else:
            f = nums.index(target)
            for i in range(f,len(nums)):
                if nums[i]>target:
                    break
                if nums[i]==target:
                    l= i
            return  [f,l]                   