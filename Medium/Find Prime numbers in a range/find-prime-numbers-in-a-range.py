#User function Template for python3

class Solution:        
    def primeRange(self,m,n):
        #code here
        k = int(math.sqrt(n))+1
        l = [1]*(n+1)
        l[0]=0
        l[1]=0
        for i in range(2,k):
            if l[i]!=0:
                for j in range(i*i,n+1,i):
                    l[j] = 0
        nw = []
        emp = []
        for i in range(m,n+1):
            if l[i] ==1:
                nw.append(i)
        return nw            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends