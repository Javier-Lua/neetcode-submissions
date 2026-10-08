from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create s1 and s2 dictionary, sliding window
        # on s2 with size len(s1), insert and delete key-value pairs
        # as sliding window moves, return true if both dicts are the same
        # else false if window reaches the end of s2, bounded by O(1)
        # because there are only lowercase letters, O(26 x 2) max = O(1)
        if len(s1) > len(s2):
            return False
        d1, d2 = Counter(), Counter()
        p1, p2 = 0, len(s1) - 1
        for i, c in enumerate(s1):
            d1[c] += 1
            d2[s2[i]] += 1
        while p2 < len(s2) - 1:
            if d2 == d1:
                return True
            d2[s2[p1]] -= 1
            if d2[s2[p1]] == 0:
                del d2[s2[p1]] 
            p1 += 1
            p2 += 1
            d2[s2[p2]] += 1
        if d2 == d1:
            return True
        return False

            