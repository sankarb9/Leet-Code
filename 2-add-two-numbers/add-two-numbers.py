# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode()
        current=dummy
        t1=l1
        t2=l2
        sum1,sum2='',''
        while t1:
            sum1+=str(t1.val)
            t1=t1.next
        while t2:
            sum2+=str(t2.val)
            t2=t2.next
        sum=str(int(sum1[::-1])+int(sum2[::-1]))
        for i in sum[::-1]:
            current.next=ListNode(int(i))
            current=current.next
        return dummy.next


