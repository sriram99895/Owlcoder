#User function Template for python3

class Solution:
    def paranthesis(self,l,r,n,s,k):
        if l == n and r == n:
            k.append(s)
            return 
        if l<n:
            self.paranthesis(l+1,r,n,s+"(",k)
        if r<l:
            self.paranthesis(l,r+1,n,s+")",k)
                
    def AllParenthesis(self,n):
        k = []
        self.paranthesis(0,0,n,"",k)
        return k
        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends