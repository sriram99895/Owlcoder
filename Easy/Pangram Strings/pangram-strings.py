#User function Template for python3
class Solution:
	def isPanagram(self, s):
		# code here
		a = "abcdefghijklmnopqrstuvwxyz"
		s = s.lower()
		d ={}
		for i in s:
		    if i in a:
		        if i not in d:
		            d[i] = 1
		        else:
		            d[i]+=1
		if len(d) == 26:
		    return 1
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends