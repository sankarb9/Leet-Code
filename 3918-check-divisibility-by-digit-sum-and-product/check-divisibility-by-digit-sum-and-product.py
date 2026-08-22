class Solution(object):
    def checkDivisibility(self, n):
        sum1=0
        product=1
        a=str(n)
        for i in range(len(str(n))):
            sum1+=int(a[i])
            product*=int(a[i])
        sum=sum1+product
        if n%sum==0:
            return True
        else:
            return False