from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterOne = Counter(s)
        counterTwo = Counter(t)
        return counterOne == counterTwo