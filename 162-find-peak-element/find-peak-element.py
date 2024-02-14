class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        k = max(nums)
        return nums.index(k)
        