# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Divide and conquer OR minheap
        # Min-heap, ingest all nodes
        # spit them all back out to result dummy head
        dummy = ListNode()
        head = dummy
        min_heap = []
        # O(n), where n is the total nodes in all lists
        curr_index = 0
        for ls in lists:
            curr_node = ls
            while curr_node is not None:
                # Python compares element by element in a tuple
                # curr_index is used as tie-breaker when two vals are the same
                heapq.heappush(min_heap, (curr_node.val, curr_index, curr_node))
                curr_node = curr_node.next
                curr_index += 1
        while min_heap:
            _, _, min_node = heapq.heappop(min_heap)
            head.next = min_node
            head = head.next
        head.next = None # Remove whatever the last node's next was
        return dummy.next