# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        arr=[]
        if not head:
            return None
        while head:
            arr.append(head.val)
            head=head.next
        k %= len(arr)
        arr=arr[-k:]+arr[:-k]
        dummy=ListNode(0)
        current=dummy
        for num in arr:
            current.next=ListNode(num)
            current=current.next
        return dummy.next

        