#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        m = 1000000007
        l = []
        a = 0
        b = 1
        l.append(a)
        l.append(b)
        for i in range(n-1):
            c = (a+b)%m
            l.append(c)
            a = b
            b = c
        return l    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends