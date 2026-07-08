# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        for i in range(0,len(arr)-1,2):
            arr[i],arr[i+1]=arr[i+1],arr[i]
        dummy=ListNode(0)
        current=dummy
        for num in arr:
            current.next=ListNode(num)
            current=current.next
        return dummy.next