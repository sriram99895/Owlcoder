class Solution:
    def printMinIndexChar(self, s, patt):
		#Code here
		for i in range(len(s)):
		    if s[i] in patt:
		        return s[i]
		return '$'        


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	S = input().strip()
    	patt = input().strip()
    	obj = Solution()
    	print(obj.printMinIndexChar(S, patt))
# } Driver Code Ends