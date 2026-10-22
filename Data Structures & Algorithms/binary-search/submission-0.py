class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search, check middle, if target < middle, search left,
        # else search right, can be faster using left, right instead of
        # array slicing
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, left, right, nums, target):
        mid = (right + left) // 2
        if left > right:
            return -1
        if nums[mid] == target:
            return mid
        else:
            if target < nums[mid]:
                return self.binary_search(left, mid - 1, nums, target)
            else:
                return self.binary_search(mid + 1, right, nums, target)
        