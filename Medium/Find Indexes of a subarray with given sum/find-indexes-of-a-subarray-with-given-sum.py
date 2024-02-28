#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,l, n, k): 
       #Write your code here
        prefix = []
        # k = int(input())
        s= 0
        d ={}
        for i in l:
            s+=i
            prefix.append(s)
        # print(prefix) 
        lent = []
        for i in range(n):
            if prefix[i] == k:
                # print(l[0:i+1])
                return [1,i+1]
            elif prefix[i] - k in d:
            #   print( l[d[prefix[i] - k]+1:i+1])
                return [d[prefix[i]-k]+2,i+1]
            else:
                d[prefix[i]] = i 
        return [-1] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends