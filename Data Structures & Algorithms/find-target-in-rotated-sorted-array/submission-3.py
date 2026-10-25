class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._binary_search(nums, 0, len(nums) - 1, target)

    def _binary_search(self, nums, left, right, target):
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Ensure when mid - 1 does not go below 0
        elif left == right or mid < 0:
            return -1
        else:
            if nums[mid] > nums[right]:
                # everything before mid is correctly 
                # sorted in increasing order
                if target < nums[mid] and target >= nums[left]:
                    return self._binary_search(nums, left, mid - 1, target)
                else:
                    return self._binary_search(nums, mid + 1, right, target)
            else:
                # everything after mid is correctly
                # sorted in increasing order
                if target > nums[mid] and target <= nums[right]:
                    return self._binary_search(nums, mid + 1, right, target)
                else:
                    return self._binary_search(nums, left, mid - 1, target)
                
                