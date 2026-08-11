class Solution(object):
    def missingInteger(self, nums):
        # Find the sequential prefix
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find the smallest integer >= total that is not in nums
        while total in nums:
            total += 1

        return total