#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        d = {}
        l =[]
        for i in arr:
            if i not in d:
                l.append(i)
                d[i] = 1
        return l
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends