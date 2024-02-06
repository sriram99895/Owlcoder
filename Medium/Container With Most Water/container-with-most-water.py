#User function Template for python3



def maxArea(a,le):
    i = 0
    j = le-1
    m = 0
    while i<j:
        t = min(a[i],a[j])*(j-i)
        m = max(m,t)
        if a[i]<a[j]:
            i+=1
        elif a[j]<a[i]:
            j-=1
        else:
            i+=1
            j-=1
    return m        
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends