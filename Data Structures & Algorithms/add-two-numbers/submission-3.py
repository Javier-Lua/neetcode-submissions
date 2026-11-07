# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Keep a carry variable, set it to 0 initially
        # Iterate through both linked lists
        # add both nodes together, resulting 
        # value is (res % 10) + carry, and carry is
        # 1 if value > 9 else 0
        # Create a new node with the new value
        p1, p2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        res = dummy
        while p1 is not None and p2 is not None:
            val = (p1.val + p2.val + carry) % 10
            carry = 1 if (p1.val + p2.val + carry) > 9 else 0
            p1, p2 = p1.next, p2.next
            res.next = ListNode(val)
            res = res.next
        if p1 is None and p2 is not None:
            while p2 is not None:
                val = (p2.val + carry) % 10 
                carry = 1 if (p2.val + carry) > 9 else 0
                res.next = ListNode(val)
                res = res.next
                p2 = p2.next
        if p2 is None and p1 is not None:
            while p1 is not None:
                val = (p1.val + carry) % 10
                carry = 1 if (p1.val + carry) > 9 else 0
                res.next = ListNode(val)
                res = res.next
                p1 = p1.next
        if carry == 1:
            res.next = ListNode(carry)
            res = res.next
        return dummy.next
