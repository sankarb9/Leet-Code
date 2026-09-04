class Solution(object):
    def firstStableIndex(self, nums, k):
        min1=99999
        for i in range(len(nums)):
            a=max(nums[0:i+1])-min(nums[i:])
            if a<=k:
                min1=min(min1,i)
        return min1 if min1!=99999 else -1