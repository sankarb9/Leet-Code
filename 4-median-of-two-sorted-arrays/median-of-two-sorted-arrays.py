class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        temp=sorted(nums1+nums2)
        n=len(temp)
        if n%2!=0:
            return temp[n//2]
        else:
            return (temp[n//2]+temp[(n//2)-1])/2.0
