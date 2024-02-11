#User function Template for python3

class Solution:
    def recamanSequence(self, n):
        # code here
        l = []
        l.append(0)
        d = {0:1}
        for i in range(1,n):
            s = l[i-1]-i
            if s > 0 and s not in d:
                l.append(s)
                d[s]=1
            else:
                k = l[i-1]+i
                l.append(k)
                d[k] = 1

        # l.extend(d.values())
        return l           
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends