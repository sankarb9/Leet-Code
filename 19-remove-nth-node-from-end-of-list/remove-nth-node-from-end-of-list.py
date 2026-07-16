# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        temp=head
        current=head
        while current:
            current=current.next
            count+=1
        if  count==n:
            return head.next
        for i in range(count-n-1):
            temp=temp.next
        temp.next=temp.next.next
        return head