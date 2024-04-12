class Solution:
    def numberGame(self, l: List[int]) -> List[int]:
        l.sort()
        k = []
        for i in range(1,len(l),2):
            k.append(l[i])
            k.append(l[i-1])
        return k    