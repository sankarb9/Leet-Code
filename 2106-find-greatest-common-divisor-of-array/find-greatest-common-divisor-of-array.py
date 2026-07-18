class Solution(object):
    def findGCD(self, nums):
        temp=set()
        max1=max(nums)
        min1=min(nums)
        for j in range(1,max(nums)+1):
            if max1%j==0 and min1%j==0:
                temp.add(j)
        temp=list(temp)
        
        return max(temp)  