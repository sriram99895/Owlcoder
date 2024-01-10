class Solution:
    def subArraySum(self,l, n, k): 
        
       #Write your code here
        # l = list(map(int,input().split()))
        prefix = []
        # k = int(input())
        s= 0
        d ={}
        for i in l:
            s+=i
            prefix.append(s)
        # print(prefix) 
        lent = []
        for i in range(n):
            if prefix[i] == k:
                # print(l[0:i+1])
                return [1,i+1]
            elif prefix[i] - k in d:
            #   print( l[d[prefix[i] - k]+1:i+1])
                return [d[prefix[i]-k]+2,i+1]
            else:
                d[prefix[i]] = i 
        return [-1]