class Solution(object):
    def maxProduct(self, n):
        temp=[]
        for i in str(n):
            temp.append(int(i))
        temp.sort()
        return temp[len(temp)-1]*temp[len(temp)-2]
                