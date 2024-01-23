#User function Template for python3

class Solution:
    def subsets(self, arr):
        #code here
        n = len(arr)
        ans = []
        for i in range(1<<n):
            l = []
            for j in range(n):
                if(i>>j)&1:
                    l.append(arr[j])
            ans.append(l)
        ans.sort()
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        A = list(map(int,input().strip().split()))
        
        ob=Solution()
        result =ob.subsets(A)
        
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j],end=" ")
                
            print()
            
            

# } Driver Code Ends