#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        d ={}
        ind = 999999
        for i in range(n):
            if arr[i] in d:
                ind = min(ind, d[arr[i]])
            else:
                d[arr[i]] = i;
                
        if ind == 999999:
            return -1
        else:
            return ind+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends