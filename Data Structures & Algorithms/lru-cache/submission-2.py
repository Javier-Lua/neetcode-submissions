class ListNode:

    def __init__(self, key, val, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key

class LRUCache:

    # Requirements: Remove an element in O(1), add to the front and back
    # in O(1) -> Doubly linked list + dictionary lookup

    def __init__(self, capacity: int):
        self.mapping = {}
        self.capacity = capacity
        self.tail, self.head = ListNode(None, 0), ListNode(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        # lookup hashmap for the node, if no node, return -1
        # remove node from linked list, then add it to tail
        # as LRU node is updated. Then return the value of the node
        node = self.mapping.get(key)
        if node is None:
            return -1
        else:
            self._remove(node)
            self._add_to_tail(node)
            return node.val


    def put(self, key: int, value: int) -> None:
        # if key exists in mapping, update mapping
        # shift node to tail
        # else, create new ListNode(key, value)
        # if self.size == self.capacity,
        # lru = self.head.next, remove lru, del mapping[lru.key]
        # self.size -= 1, add new node to tail, and
        # add to mapping, increment size by one
        if key in self.mapping:
            old_node = self.mapping[key]
            self.mapping[key] = ListNode(key, value)
            self._remove(old_node)
            self._add_to_tail(self.mapping[key])
        else:
            node = ListNode(key, value)
            if self.size == self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.mapping[lru.key]
                self.size -= 1
            self._add_to_tail(node)
            self.mapping[key] = node
            self.size += 1

    def _remove(self, node):
        # Remove node from its current position
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None

    def _add_to_tail(self, node):
        # Insert node immediately BEFORE the dummy tail
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node


