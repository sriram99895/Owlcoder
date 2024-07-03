class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=4:
            return 0
        nums.sort()
        mi,ma = min(nums),max(nums)
        k = ma-nums[3]
        k2 = nums[n-4]-mi
        k3 = nums[n-3]-nums[1]
        k4 = nums[n-2] - nums[2]
        return min(k,k2,k3,k4)




        