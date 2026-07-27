class Solution(object):
    def maxProduct(self, nums):
        n=len(nums)
        nums.sort()
        return (nums[n-1]-1)*(nums[n-2]-1)