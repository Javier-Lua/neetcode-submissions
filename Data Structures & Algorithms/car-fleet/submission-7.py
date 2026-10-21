class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip position and speed, then sort them by position, smallest first
        res = sorted(list(zip(position, speed)), key = lambda p: p[0])
        # (target - position) / speed?
        steps = []
        for pos, sp in res:
            steps.append((target - pos) / sp)
        stack = []
        # stack should only contain unique car fleets
        for i in range(1, len(steps) + 1):
            if not stack:
                stack.append(steps[-i])
            if steps[-i] <= stack[-1]: 
                # if previous car completes faster, 
                # it joins the fleet of the car in front
                continue
            else:
                stack.append(steps[-i])
        return len(stack)