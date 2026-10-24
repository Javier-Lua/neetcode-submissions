class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Goal: Find the min -> A min element is
        # when both elements adjacent to it is
        # higher than itself. O(logn) using binary search
        return self._binary_search(nums, 0, len(nums) - 1)
    
    def _binary_search(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        # minimum is in the window between mid and right
        if nums[mid] > nums[right]:
            return self._binary_search(nums, mid + 1, right)
        else:
            return self._binary_search(nums, left, mid)
        