#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,arr, n): 
        ##Your code here
        mi = arr[0]
        minarr = [mi]
        for i in range(1,n):
            mi = min(arr[i],mi)
            minarr.append(mi) 
        # print(minarr)
        ma = arr[-1]
        maxarr = [ma]
        for i in range(n-2,-1,-1):
            ma = max(ma,arr[i])
            maxarr.append(ma)
        # print(maxarr)    
        maxarr.reverse()
        mainmax = -1
        i = 0
        j = 0
        while i<n and j<n:
            if minarr[i]<=maxarr[j]:
                mainmax= max(j-i,mainmax)
                j+=1
            else:
                i+=1
        return mainmax 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends