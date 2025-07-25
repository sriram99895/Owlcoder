class Solution:
    def maxSum(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        s = 0
        for k,v in d.items():
            if k>=0:
                s+=k
        if s==0:
            return max(d.keys())
        return s                    
        