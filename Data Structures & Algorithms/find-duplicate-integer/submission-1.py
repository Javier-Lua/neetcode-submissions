class Solution:
    # Relook
    def findDuplicate(self, nums: List[int]) -> int:
        # fast and slow pointers, will meet when
        # a cycle exists, i.e. duplicate integers
        # reset the slow pointer to the start, and move both
        # pointers one at a time, and when they meet again
        # that is the entrance of the cycle, which is the duplicate
        # integer, each array index is a unique node, where index i
        # points to nums[i], entrance's index is the duplicate value
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
        