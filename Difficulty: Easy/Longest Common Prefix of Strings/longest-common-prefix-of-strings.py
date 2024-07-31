#User function Template for python3

class Solution:
    def longestCommonPrefix(self, strs):
        # code here
        sp = strs[0]
        m = 999999
        for i in strs:
            m = min(m,len(i))
        # print(m)    
        k = sp[:m]
        ma =99999
        for i in strs:
            c = 0
            for j in range(m):
                if i[j] == k[j]:
                    c+=1
                else:
                    break 
            if c == 0:
                return -1
            ma = min(ma,c)               
        return sp[:ma] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends