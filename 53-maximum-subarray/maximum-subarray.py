class Solution(object):
    def maxSubArray(self, nums):
        currentsum=0
        maxSum=nums[0]
        for num in nums:
            currentsum+=num
            maxSum=max(maxSum,currentsum)
            if currentsum<0:
                currentsum=0
        return maxSum