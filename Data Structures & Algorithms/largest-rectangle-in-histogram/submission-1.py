class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # For every height in heights,
        # append to the stack if current height > peek
        # else, pop element from the stack, reduce index
        # of current height by one, while loop. At every
        # pop, update 
        # max area = popped height * (curr ind - popped ind)
        # At the end of the iteration, elements
        # containing the stack can reach to the end
        # of the histogram, iterate through remaining
        # elements, update max area by len(heights) - index
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            start = i
            while stack and height <= stack[-1][1]:
                ind, ht = stack.pop()
                max_area = max(ht * (i - ind), max_area)
                start = ind
            stack.append((start, height))
        for pos, height in stack:
            max_area = max(max_area, height * (len(heights) - pos))
        return max_area
