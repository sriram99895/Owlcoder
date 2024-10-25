class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        n = len(arr)
        arr.sort()
        l = []
        for i in range(n//2):
            l.append(arr[n-i-1])
            l.append(arr[i])
        if n%2 == 1:
            l.append(arr[n//2])
        return l    
#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends