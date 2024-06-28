class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0]*(n)
        for k,v in roads:
            arr[k]+=1
            arr[v]+=1
        arr.sort()
        s = 0
        for i in range(n):
            s+=arr[i]*(i+1)
        return s        

        