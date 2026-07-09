class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy=ListNode(0)
        current=dummy
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        left -= 1
        right -= 1

        arr = arr[:left] + arr[left:right+1][::-1] + arr[right+1:]
        for num in arr:
            current.next=ListNode(num)
            current=current.next
        return dummy.next

                

                