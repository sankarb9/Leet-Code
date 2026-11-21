# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        crr=head
        while crr and crr.next:
            if crr.val== crr.next.val:
                crr.next=crr.next.next
            else:
                crr=crr.next
        return head
