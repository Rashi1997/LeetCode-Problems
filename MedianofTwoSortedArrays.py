class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1len=len(nums1)
        nums2len=len(nums2)
        if(nums1len>nums2len):
            nums1,nums2=nums2,nums1
            nums1len,nums2len=nums2len,nums1len
        imin=0
        imax=nums1len
        while imin<=imax:
            i=(imin+imax)//2
            j=int(((nums1len+nums2len +1)/2)-i)
            if i<nums1len and nums2[j-1]>nums1[i]:
                imin=i+1
            elif i>0 and nums1[i-1]>nums2[j]:
                imax=i-1
            else:
                if i==0:
                    maxfromleft=nums2[j-1]
                elif j==0:
                    maxfromleft=nums1[i-1]
                else:
                    maxfromleft=max(nums2[j-1],nums1[i-1])
                if (nums1len+nums2len)%2==1:
                    return float(maxfromleft)
                if i==nums1len:
                    minfromright = nums2[j]
                elif j == nums2len:
                    minfromright = nums1[i]
                else: 
                    minfromright = min(nums1[i], nums2[j])
                return (maxfromleft + minfromright) / 2.0
