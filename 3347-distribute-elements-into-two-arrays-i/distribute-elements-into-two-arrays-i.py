class Solution(object):
    def resultArray(self, nums):
        temp=[]
        temp2=[]
        temp.append(nums[0])
        temp2.append(nums[1])
        for i in range(len(nums)):
            if i==0 or i==1:
                continue
            else:
                if temp[len(temp)-1]>temp2[len(temp2)-1]:
                    temp.append(nums[i])
                else:
                    temp2.append(nums[i])
        return temp+temp2
        