class Solution(object):
    def threeSum(self, nums):
        i=0
        left=i+1
        right=len(nums)-1
        nums.sort()
        temp=set()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1

            while left<right:
                sum1=nums[i]+nums[left]+nums[right]
                if sum1==0:
                    temp.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif sum1<0:
                    left+=1
                else:
                    right-=1
        return [list(x) for x in temp]
            