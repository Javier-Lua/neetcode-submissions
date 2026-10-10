import heapq
from typing import List

class Solution:
    # RELOOK
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, k - 1
        heap = [(-x, i) for i, x in enumerate(nums[:k])]
        heapq.heapify(heap)
        res = []

        max_element = heap[0]
        max_value = -max_element[0]
        max_idx = max_element[1]
        res.append(max_value)

        while right < len(nums) - 1:
            left += 1
            right += 1

            heapq.heappush(heap, (-nums[right], right))

            while heap[0][1] < left:
                heapq.heappop(heap)

            max_element = heap[0]
            max_value = -max_element[0]
            max_idx = max_element[1]
            res.append(max_value)

        return res