class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = len(nums1)
        b = len(nums2)
        nums1.sort()
        nums2.sort()
        l = []
        i = j = 0
        while i<a and j<b:
            if nums1[i] == nums2[j]:
                l.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return l                
        