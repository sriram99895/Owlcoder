class Solution:
    #convert an aarry into 2d array
    def findMatrix(self, l: List[int]) -> List[List[int]]:
        n = len(l)
        # l = list(map(int,input().split()))
        d = {}
        for i in l:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        k = max(d.values()) 
        arr = []
        for i in range(k):
            arr.append([])
        # print(arr)
        for i in range(n):
            for j in range(len(arr)):
                if l[i] not in arr[j]:
                    arr[j].append(l[i])
                    break
                if l[i] in arr[j]:
                    continue
        return arr