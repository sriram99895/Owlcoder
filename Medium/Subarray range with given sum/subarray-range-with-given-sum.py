#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, n, k):
        #Your code here
        p= 0
        d ={}
        c = 0
        for i in arr:
            p+=i
            if p == k:
                c+=1
            if p-k in d:
                c+=d[p-k]
            if p in d:
                d[p]+=1
            else:
                d[p]=1
        return c        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        sum=int(input())
        
        print(Solution().subArraySum(arr, n, sum))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends