#User function Template for python3

class Solution:
    def Solve(self, n, a):
        # Code here
        d ={}
        # k = int(math.ceil(n//3))
        for i in a:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        l = []        
        for k,v in d.items():
            if v>n//3:
                l.append(k)
        if len(l) == 0:
            return [-1]
        return l
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        res = ob.Solve(n, a)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends