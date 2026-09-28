class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## height of water in container == min(left, right)
        ## total area = max(left, right) * (right - left)
        p1, p2 = 0, len(heights) - 1
        max_area = 0
        while p1 < p2:
            height = min(heights[p1], heights[p2])
            area = height * (p2 - p1)
            if (area > max_area):
                max_area = area
            if (heights[p1] < heights[p2]):
                p1 += 1
            else:
                p2 -= 1
        return max_area
