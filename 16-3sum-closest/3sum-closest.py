class Solution:
    def threeSumClosest(self, l: List[int], target: int) -> int:
        l.sort()
        n = len(l)
        s = l[0]+l[1]+l[2]
        for i in range(n):
            j = i+1
            k = n-1
            while j<k:
                ns = l[i] + l[j]+l[k]
                if ns == target:
                    return ns
                elif ns<target:
                    if abs(ns-target) <= abs(s - target):
                        s = ns
                    j+=1
                else:
                    if abs(ns - target)<= abs(s-target):
                        s = ns
                    k-=1
        return s  
        