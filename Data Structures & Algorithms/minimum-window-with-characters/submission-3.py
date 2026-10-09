class Solution:

    # Can be improved by replacing slicing s[left: right + 1] with window length
    def minWindow(self, s: str, t: str) -> str:
        # Have and Need variables as counters
        # to check number of unique letters we have
        # and number of unique letters we need
        # need stays unchanged once initialised with t
        # Keep two hash maps for each variable, Have and 
        # Need, when we have a letter we need, update Have
        # and its corresponding hashmap, and check whether
        # its value is equal to the letter in Need's hashmap,
        # if yes, increment have by 1.
        # Keep two pointers as ends of a sliding window
        # right moves until Have == Need, and left moves
        # until Have < Need, and as left moves, record the
        # best current min_substring.
        # Total variables, 2 hashmaps, 5 additional variables
        # Need and need stays unchanged throughout, and should count unique characters
        need, have = Counter(t), Counter()
        Need, Have = len(need), 0
        left = 0
        min_substring = ""
        for right in range(len(s)):
            # Always Run right, because iteration only moves when left is done
            if s[right] in need:
                have[s[right]] += 1
                if have[s[right]] == need[s[right]]:
                    Have += 1
            # Run left
            while Have == Need: # Hit, then record min substring
                if len(min_substring) > len(s[left:right + 1]) \
                                or min_substring == "":
                            min_substring = s[left:right + 1]
                if s[left] in need:
                    have[s[left]] -= 1
                    if have[s[left]] < need[s[left]]:
                        Have -= 1
                    if have[s[left]] == 0:
                        del have[s[left]]
                left += 1
        return min_substring