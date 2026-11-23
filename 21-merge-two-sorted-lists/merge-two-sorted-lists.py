# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode()
        current=dummy
        t1=list1
        t2=list2
        while t1 and t2:
            if t1.val<t2.val:
                current.next=ListNode(t1.val)
                current=current.next
                t1=t1.next
            elif t1.val>=t2.val:
                current.next=ListNode(t2.val)
                current=current.next
                t2=t2.next
        if t2 is None:
            current.next=t1
        else:
            current.next=t2
        return dummy.next
         

            
