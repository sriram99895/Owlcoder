class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        c = 1
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i] == nums[j] and i!=j and (i*j)%k == 0 and i<j:
                    c+=1
        return c-1            

        