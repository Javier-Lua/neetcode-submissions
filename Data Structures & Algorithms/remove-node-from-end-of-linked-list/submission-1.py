# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # p1 traverses the linkedlist until it hits the end,
        # counting the count of nodes. Once done, calculate
        # target position, and use that to tell how much
        # p2 should traverse to hit the target node
        # then set target node - 1's next to next.next,
        # and set target node's next to None, then return
        # the head
        p1, p2 = head, head
        count = 0 
        # count is set to 0 because the last node's next is None,
        # which increases count
        while p1 is not None:
            p1 = p1.next
            count += 1
        if n == count:
            return head.next
        needed_jumps = count - n - 1
        curr_jumps = 0
        while curr_jumps < needed_jumps:
            p2 = p2.next
            curr_jumps += 1
        if p2 is not None:
            target = p2.next
            p2.next = target.next
            target.next = None
            return head

