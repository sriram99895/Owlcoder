#User function Template for python3

class Solution:
    def findSubArraySum(self, l, n, k):
        # code here
        d = {}
        p = 0
        c =0
        for i in l:
            p+=i
            if p == k:
                c+=1
            if p-k in d:
                c+=d[p-k]
            if p in d:
                d[p]+=1
            else:
                d[p] = 1
        return c        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.findSubArraySum(Arr, N, k))
# } Driver Code Ends