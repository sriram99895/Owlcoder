#User function Template for python3



def findMissing(A,B,N,M):
    # code here
    l = []
    d = {}
    for i in B:
        d[i] = 1
    for i in A:
        if i not in d:
            l.append(i)
    return l        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
   # n=int(input())
    l = list(map(int, input().split()))
    n=l[0]
    m=l[1]
    a = list(map(int,input().split()))
    b = list(map(int, input().split()))
    ans=findMissing(a,b,n,m)
    for each in ans:
        print(each,end=' ')
    print()
# } Driver Code Ends