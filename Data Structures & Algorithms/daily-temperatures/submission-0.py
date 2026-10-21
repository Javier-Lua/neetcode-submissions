class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack, push temperatures with their index
        # onto the stack, if the current temperature is higher
        # than peek, pop and record difference in indices
        # do this until the current temperature is NOT higher than
        # peek, then push that temperature into the stack
        # anything left in the stack
        # the entry is 0 in res for that index.
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            while stack and temp > stack[-1][-1]:
                peek = stack.pop()
                res[peek[0]] = i - peek[0]
            stack.append((i, temp))
        return res
