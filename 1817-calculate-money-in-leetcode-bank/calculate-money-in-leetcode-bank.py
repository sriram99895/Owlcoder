class Solution:
    def totalMoney(self, n: int) -> int:
            k = n//7
            l = k
            i = 0
            s = 0
            r = n%7
            while(k):
                print(28+(7*i))
                s+=28+(7*i)
                k = k-1
                i+=1
            l = l+1
            for i in range(r):
                s+=l
                l+=1

            return s  
        