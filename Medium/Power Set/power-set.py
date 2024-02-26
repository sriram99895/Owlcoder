#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		emp = []
        n = len(s)
        for i in range(1,2**n):
            k = ""
            for j in range(n):
                if (i>>j)&1>0:
                    k+=s[j]
            emp.append(k)
        emp.sort()
        return emp 


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends