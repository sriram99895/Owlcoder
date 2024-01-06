#minimum number of operations required to make number equal to k
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        c = 0
        x =0
        for i in range(len(nums)):
            x = x^nums[i]    
        for i in range(32):
            if ((x>>i)&1 > 0) and ((k>>i)&1 == 0):
                c+=1
            elif ((x>>i)&1 == 0) and ((k>>i)&1 >0):
                c+=1
            else:
                c+=0
        return c   
l = list(map(int,input().split()))
k = int(input())
print(minOperations(l,k))        