"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Keep a dictionary mapping, keys as the original nodes
        # values as the new copied nodes of its respective keys
        # Iterate through the linked list and create key-value pairs
        # copies with the values can be created. Iterate through the
        # original linked list again, and for every original node,
        # look up the copied node in the dictionary, as well as the
        # copied next node, and the copied random node tied to the original
        # node. Then assign the copied node's next and random to those copied nodes
        mapping = {None: None} # When a mapping looks up with "None" -> mapping[None]
        p1, p2 = head, head
        while p1 is not None:
            mapping[p1] = Node(p1.val)
            p1 = p1.next
        while p2 is not None:
            copied_p2 = mapping[p2]
            copied_p2_next = mapping[p2.next]
            copied_p2_random = mapping[p2.random]
            copied_p2.next = copied_p2_next
            copied_p2.random = copied_p2_random
            p2 = p2.next
        return mapping[head]




