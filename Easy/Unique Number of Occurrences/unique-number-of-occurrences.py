
from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, l: List[int]) -> bool:
        # code here
        d = {}
        f=[]
        for i in l:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for v in d.values():
            f.append(v)
        ne = []
        for i in f:
            if i not in ne:
                ne.append(i)
        if ne == f:
            return  1
        return 0    
        
        



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.isFrequencyUnique(n, arr)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends