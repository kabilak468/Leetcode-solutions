class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1=sorted(nums1+nums2)
        check=len(nums1)//2
        n=len(nums1)%2
        if n!=0:
            res=nums1[check]
        if n==0:
            res=(nums1[check]+nums1[check-1])/2
        return res  