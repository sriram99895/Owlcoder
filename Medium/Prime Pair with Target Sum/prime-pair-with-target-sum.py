
from typing import List
import math


class Solution:
    def getPrimes(self, n : int) -> List[int]:
        # code here
        k = int(math.sqrt(n))+1
        l = [1]*(n+1)
        for i in range(2,k):
            if l[i]!=0:
                for j in range(i*i,n+1,i):
                    l[j] = 0
        nw = []
        emp = []
        for i in range(2,n+1):
            if l[i] ==1:
                nw.append(i)
        i = 0
        j = len(nw)-1
        while i<=j:
            if nw[i]+nw[j] == n:
                return [nw[i],nw[j]]
            elif nw[i]+nw[j]>n:
                j = j-1
            elif nw[i]+nw[j]<n:
                i+=1
            else:
                i+=1
                j+=1
        return [-1,-1]        
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.getPrimes(n)

        IntArray().Print(res)

# } Driver Code Ends