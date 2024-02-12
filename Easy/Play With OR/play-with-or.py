#User function Template for python3

def game_with_number (l,  n) : 
    #Complete the function
    prev = l[0]
    for i in range(1,n):
        l[i-1] = prev|l[i]
        prev = l[i]
    return l 


#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends