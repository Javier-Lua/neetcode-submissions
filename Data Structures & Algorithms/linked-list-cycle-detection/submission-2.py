# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = ListNode(0), head
        slow.next = head
        while fast is not None:
            if slow != fast:
                slow = slow.next
                fast = fast.next
                if fast is None:
                    return False
                else:
                    fast = fast.next
            else:
                return True
        return False
