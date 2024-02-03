#User function Template for python3

#Back-end complete function Template for Python 3

class Solution:
    def sol(self,i):
        s = 0
        while(i):
            s+=i%10
            i = i//10
        return s
    def RulingPair(self, arr, n): 
    	# Your code goes here
    	d = {}
    	for i in arr:
    	    if self.sol(i) not in d:
    	        d[self.sol(i)] = [i]
    	    else:
    	        d[self.sol(i)].append(i)
    	ma = -1
    	for k,v in d.items():
    	    v.sort()
    	    if len(v)>=2:
    	        ma = max(ma,v[-1]+v[-2])
    	return ma     
    	        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution();
        print(obj.RulingPair(arr,n))



# } Driver Code Ends