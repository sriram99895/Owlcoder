class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        for i in target:
            if i not in d:
                d[i] =1
            else:
                d[i]+=1
        for i in arr:
            if i not in d:
                return 0
            if i in d:
                if d[i] != arr.count(i):
                    return 0
        return 1            
                                

        