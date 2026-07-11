class Solution(object):
    def sortColors(self, nums):
        left=0
        right=len(nums)-1
        mid=0
        while mid<=right:
            if nums[mid]==0:
                nums[mid],nums[left]=nums[left],nums[mid]
                mid+=1
                left+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid],nums[right]=nums[right],nums[mid]
                right-=1