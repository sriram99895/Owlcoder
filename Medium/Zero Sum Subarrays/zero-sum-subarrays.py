#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        #return: count of sub-arrays having their sum equal to 0
        p = 0
        c = 0
        d ={}
        for i in arr:
            p+=i
            if p ==0:
                c+=1
            if p-0 in d:
                c+=d[p-0]
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        return c        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends