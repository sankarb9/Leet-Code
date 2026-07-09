# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        result=[]
        for i in range(0,len(arr),k):
            group=arr[i:i+k]
            if len(group) == k:
                result.extend(group[::-1])
            else:
                result.extend(group)
        dummy=ListNode(0)
        current=dummy
        for  num in result:
            current.next=ListNode(num)
            current=current.next
        return dummy.next
