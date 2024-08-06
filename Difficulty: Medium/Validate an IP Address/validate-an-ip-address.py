#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        l = s.split(".")
        # print(l)
        if len(l)<4 or len(l)>4:
            return 0
        for i in l:
            if len(i)>3:
                return 0
            if len(i) == 0:
                return 0
            if int(i)<0 or int(i)>255:
                return 0
            if len(i)>=2:
                if i[0] == '0':
                    return 0
        return 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends