class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        output=ListNode(0)
        curr=output
        carry=0
        while l1 or l2 or carry:
            
            out=(l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry=out//10
            nextnode=ListNode(out%10)
            curr.next=nextnode
            curr=nextnode
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return output.next