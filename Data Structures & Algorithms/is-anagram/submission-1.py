from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## == between arrays invokes == on every pairwise element
        ## one by one from left to right
        counterOne = Counter(s)
        counterTwo = Counter(t)
        return counterOne == counterTwo