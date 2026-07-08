# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        arr=[]
        for head in lists:
            temp=head
            while temp:
                arr.append(temp.val)
                temp=temp.next
        arr.sort()
        dummy=ListNode(0)
        current=dummy
        for num in arr:
            current.next=ListNode(num)
            current=current.next
        return dummy.next


        