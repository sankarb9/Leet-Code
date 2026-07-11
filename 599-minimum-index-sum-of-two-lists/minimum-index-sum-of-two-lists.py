class Solution(object):
    def findRestaurant(self, list1, list2):

        min_sum=float("inf")
        result=[]

        for i in range(len(list1)):
            for j in range(len(list2)):
                total=i+j
                if list1[i]==list2[j]:
                    if total<min_sum:
                        min_sum=total
                        result=[list1[i]]
                        
                    elif total==min_sum:
                        result.append(list1[i])
        return result
