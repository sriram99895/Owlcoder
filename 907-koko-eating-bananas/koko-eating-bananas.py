class Solution:
    def check(self,arr,n,h,p):
        s = 0
        for i in range(n):
            s+=math.ceil(arr[i]/p)
            if s>h:
                return 0
        return 1               

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low = 1
        high = piles[len(piles)-1]
        while low<=high:
            mid = (high+low)//2
            if self.check(piles,len(piles),h,mid):
                print(mid)
                high = mid-1
            else:
                low = mid+1
        return low           

        