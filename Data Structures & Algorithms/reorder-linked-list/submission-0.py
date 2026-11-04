# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first pointer p1 stays at head
        # second pointer p2 goes to the start
        # of the second half
        # p2 reverses the linked list from that point
        # until the end, and then when p1 is at the beginning
        # and p2 is at the end, alternate on a tail dummy
        # until everything is added, don't need to return anything
        # use fast and slow pointers to find out the start and
        # the middle list node
        slow, fast = ListNode(0), head
        slow.next = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        # slow is now at the mid-point, and slow.next is start of right partition
        start = slow.next
        slow.next = None
        end = self._reverse(start)
        start = head
        dummy = ListNode(0)
        tail = dummy
        length = 0
        while start is not None or end is not None:
            if length % 2 == 0 and start is not None:
                tail.next = start
                tail = tail.next
                start = start.next
            elif length % 2 > 0 and end is not None:
                tail.next = end
                tail = tail.next
                end = end.next
            length += 1
            
    def _reverse(self, head):
        p1, p2 = None, head
        while p2 is not None:
            next_node = p2.next
            p2.next = p1
            p1 = p2
            p2 = next_node
        return p1



        