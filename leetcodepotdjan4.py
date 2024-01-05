#minimum number of operations to make array empty
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        c = 0 
        t = 0  
        print(d)     
        for k,v in d.items():
            if v%3 == 0:
                c+=v//3
            elif (v-4) >0 and (v-4)%3 == 0:
                c+=(v-4)//3 +2
            elif v%3 == 2:
                c+=v//3+1
            elif v%2 == 0:
                c+=v//2
            else:
                return -1        
        return c 