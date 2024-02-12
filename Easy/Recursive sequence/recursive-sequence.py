#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        m = 1e9+7
        s = 0
        k = 1
        for i in range(n):
            p = 1
            for j in range(i+1):
                p =  p%m*k%m
                k+=1
            s+=p%m
        s =s%m
        return int(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends