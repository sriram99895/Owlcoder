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
s = input()
ob = Solution()
ans = ob.AllPossibleStrings(s)
print(ans)
         