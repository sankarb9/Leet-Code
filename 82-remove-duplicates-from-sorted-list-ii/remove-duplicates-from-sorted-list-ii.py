# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current=head
        tmp=ListNode()
        cr=tmp
        while current:
            if current.next is None or current.val!=current.next.val:
                cr.next=current
                cr=cr.next
                current=current.next
            else:
                val=current.val
                while current and current.val == val:
                    current=current.next
        cr.next=None
        return tmp.next