class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        while i<n and j<m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1                

        