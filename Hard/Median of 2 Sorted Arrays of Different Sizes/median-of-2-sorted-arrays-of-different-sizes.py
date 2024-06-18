#User function Template for python3

class Solution:
    def MedianOfArrays(self, nums1, nums2):
        #code here
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if len(nums1)%2 == 1:
            return nums1[n//2]
        else:
            if nums1[n//2]%2 == 0 and nums1[n//2-1]%2 == 1:
                return float("{0:.1f}".format((nums1[n//2]+nums1[n//2-1])/2))
            elif nums1[n//2]%2 == 1 and nums1[n//2-1]%2 == 0 :
                return float("{0:.1f}".format((nums1[n//2]+nums1[n//2-1])/2))
            else:
                return (nums1[n//2]+nums1[n//2-1])//2


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends