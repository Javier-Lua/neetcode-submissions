# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Reverse sets of k nodes, set the previous group's tail.next
        # to the current group's head, store the first head of the reversed
        # list to return at the end
        head, tail = self._reverse(head, k)
        new_head = head
        head = tail.next
        while head is not None:
            head, temp_tail = self._reverse(head, k)
            tail.next = head
            tail = temp_tail
            head = tail.next
        return new_head


    def _reverse(self, head, k):
        # Reverses a linkedlist for the first k nodes.
        # if the linkedlist's length is less than k
        # return (head, tail) as is, else the reversed list's (head, tail)
        p1, p2 = None, head
        next_head = None
        count = 0
        length = 0
        original_head = p2
        while head is not None:
            head = head.next
            length += 1
            if length == k:
                p1 = head
                break # Break so it maintaing O(k) runtime
        if length < k:
            return (p2, original_head)
        while p2 is not None and count < k:
            next_node = p2.next
            p2.next = p1
            p1 = p2
            p2 = next_node
            count += 1
        return (p1, original_head)
