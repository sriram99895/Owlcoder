class Solution:
    def maximumHappinessSum(self, l: List[int], k: int) -> int:
        l.sort()
        l.reverse()
        s = 0
        for i in range(k):
            if l[i]-i>0:
                s+=l[i]-i
        return s
        