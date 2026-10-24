class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search from an ascending order of hours
        # from range of 1 to max(piles), find mid, if cannot eat all
        # bananas, search right, if can, search left.
        # Logic to determine whether k b/hr can eat all:
        # sum up hours per element, if k >= element, add 1,
        # else, add math.ceil(ele / k).
        return self.binary_search(piles, 1, max(piles), h)
    
    def binary_search(self, piles, left, right, h):
        mid = (left + right) // 2
        if left == right:
            return left
        elif self.can_eat(mid, piles, h):
            return self.binary_search(piles, left, mid, h)
        else:
            return self.binary_search(piles, mid + 1, right, h)

    def can_eat(self, k, piles, h):
        res = 0
        for pile in piles:
            res += math.ceil(pile / k)
        return res <= h