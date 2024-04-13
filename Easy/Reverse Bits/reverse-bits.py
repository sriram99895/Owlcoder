#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        n = 0
        for i in range(32):
            n = n|(x&1)
            n = n<<1
            x = x>>1
        return n>>1           

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends