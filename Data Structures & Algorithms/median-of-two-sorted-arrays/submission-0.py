import math

class Solution:
    # left starts at -1 because there can be no left partition in target array
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        target = nums1 if len(nums1) < len(nums2) else nums2
        other = nums1 if len(nums1) >= len(nums2) else nums2
        return self._binary_search(-1, len(target) - 1, target, other)

    def _binary_search(self, left, right, target, other):
        mid = (left + right) // 2
        total_elements = len(target) + len(other)
        # (mid + 1) + (other_index + 1) = (total_elements + 1) // 2
        target_index, other_index = mid, (total_elements + 1) // 2 - mid - 2

        target_element = target[target_index] if target_index >=0 else -math.inf
        other_element = other[other_index] if other_index >=0 else -math.inf

        target_next = target[target_index + 1] if target_index + 1 < len(target) else math.inf
        other_next = other[other_index + 1] if other_index + 1 < len(other) else math.inf
        if target_element <= other_next and other_element <= target_next:
            if total_elements % 2 == 0:
                return (max(target_element, other_element) + \
                    min(other_next, target_next)) / 2
            else:
                return max(target_element, other_element)
        elif target_element > other_next:
            return self._binary_search(left, mid - 1, target, other)
        else:
            return self._binary_search(mid + 1, right, target, other)
                
                    



