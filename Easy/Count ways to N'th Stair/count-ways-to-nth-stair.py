#User function Template for python3


class Solution:

    #Function to count number of ways to reach the nth stair
    #when order does not matter.
    def countWays(self, n):

        mod = 1000000007
        # code here
        c = 1
        while (n>1):
            c+=1
            n = n-2
        # print(c)
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        ob = Solution()
        print(ob.countWays(n))

# } Driver Code Ends