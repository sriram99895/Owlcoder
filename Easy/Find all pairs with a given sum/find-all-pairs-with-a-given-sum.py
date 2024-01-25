#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, x):
        # Your code goes here 
        d = {}
        A.sort()
        B.sort()
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        l = []        
        for i in B:
            if x - i in d:
                for p in range(d[x-i]):
                    l.append([x-i,i])
        l.sort()        
        return l        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
        	print(-1) 
        
        else: 
            
        	for i in range(sz):
        		if i==sz-1:
        		    print(*answer[i])
        		else:
        		    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()




# } Driver Code Ends