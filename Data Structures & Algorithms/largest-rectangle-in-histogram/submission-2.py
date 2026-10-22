class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][1]:
                ind, ht = stack.pop()
                max_area = max(ht * (i - ind), max_area)
                start = ind
            stack.append((start, height))
        for pos, height in stack:
            max_area = max(max_area, height * (len(heights) - pos))
        return max_area