#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        # code here
        k=""
        for i in range(r):
            for j in range(n+1):
                if s[j] == '1':
                    k+='10'
                else:
                    k+='01'
            s = k 
            k = ""
        return s[n]    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends