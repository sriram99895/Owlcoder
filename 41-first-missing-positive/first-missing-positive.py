class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        l = [0]*(n+1)
        for i in nums:
            if i > 0 and i<=n:
                l[i] = 1
        for i in range(1,n+1):
            if l[i] == 0:
                return i
        return n+1                