# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        count,count1=0,0
        while temp:
            count+=1
            temp=temp.next
        temp=head
        while temp:
            count1+=1
            if count1==(count-n) and (count-n) !=0:
                temp.next=temp.next.next
            elif (count-n)==0:
                return head.next
            else:
                temp=temp.next
        return head
