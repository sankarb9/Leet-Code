# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        current=head
        temp=ListNode()
        temp2=ListNode()
        cr=temp
        cr2=temp2
        while current:
            if current.val<x:
                cr.next=current
                cr=cr.next
            elif current.val>=x:
                cr2.next=current
                cr2=cr2.next
            current=current.next
        cr2.next=None
        cr.next=temp2.next
        return temp.next