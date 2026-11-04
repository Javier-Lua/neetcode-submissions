# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node and set that as the tail of the result
        # p1, p2 as pointers at the head of each linked list
        # attach tail.next to the min(p1.val, p2.val)
        # repeat until BOTH p1 and p2 are none
        dummy = ListNode(0)
        tail = dummy
        p1, p2 = list1, list2
        while p1 is not None or p2 is not None:
            if p1 is None:
                tail.next = p2
                p2 = p2.next
            elif p2 is None:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p1 if p1.val < p2.val else p2
                if tail.next == p1:
                    p1 = p1.next
                else:
                    p2 = p2.next
            tail = tail.next
        return dummy.next
