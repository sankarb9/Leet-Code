class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        temp=[]
        for i in nums1:
            a=nums2.index(i)
            for j in range(a+1,len(nums2)):
                if i<nums2[j]:
                    temp.append(nums2[j])
                    break
            else:
                temp.append(-1)
        return temp