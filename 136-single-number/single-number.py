class Solution(object):
    def singleNumber(self, nums):
        a = 0
 
        for x in nums:
            a ^= x
 
        return a