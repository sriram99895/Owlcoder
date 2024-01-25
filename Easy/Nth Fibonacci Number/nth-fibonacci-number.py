m = 1e9+7
class Solution:
    # def fib(self,n):
    #     if n==0 or n==1:
    #         return n
    #     return (self.fib(n-1)%m + self.fib(n-2)%m )%m   
    def nthFibonacci(self, n : int) -> int:
        # code herek 
        a = 0
        b =1
        for i in range(1,n):
            c = a%m+b%m
            a = b
            b = c
        return int(c%m)        
        
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends